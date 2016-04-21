var bb_height_eqns = {};

bb_height_eqns.init = function() {
  this.defined = [];
  this.latest_defined = [];

  this.define = function(name) {
    this.defined.push(name);
  };

  this.inputs_required = 3;

  this.params = {
    wheel_diameter: undefined,
    wheel_radius: undefined,
    crank_arm_length: undefined,
    bb_height: undefined,
    pedal_clearance: undefined,
    bb_drop: undefined,
  };

  this.calculate = function() {
    var l = this.defined.length;
    this.latest_defined = this.defined.slice(l-this.inputs_required,l);

    if (false) {
    }
    else if (isEqArrays(this.latest_defined, ['wheel_diameter', 'crank_arm_length', 'bb_height', ])) {
      this.params.bb_drop = -this.params.bb_height + this.params.wheel_diameter/2
      this.params.pedal_clearance = this.params.bb_height - this.params.crank_arm_length
      this.params.wheel_radius = this.params.wheel_diameter/2
    }
    else if (isEqArrays(this.latest_defined, ['wheel_diameter', 'crank_arm_length', 'pedal_clearance', ])) {
      this.params.bb_drop = -this.params.crank_arm_length - this.params.pedal_clearance + this.params.wheel_diameter/2
      this.params.wheel_radius = this.params.wheel_diameter/2
      this.params.bb_height = this.params.crank_arm_length + this.params.pedal_clearance
    }
    else if (isEqArrays(this.latest_defined, ['wheel_diameter', 'crank_arm_length', 'bb_drop', ])) {
      this.params.pedal_clearance = -this.params.bb_drop - this.params.crank_arm_length + this.params.wheel_diameter/2
      this.params.wheel_radius = this.params.wheel_diameter/2
      this.params.bb_height = -this.params.bb_drop + this.params.wheel_diameter/2
    }
    else if (isEqArrays(this.latest_defined, ['wheel_diameter', 'bb_height', 'pedal_clearance', ])) {
      this.params.bb_drop = -this.params.bb_height + this.params.wheel_diameter/2
      this.params.crank_arm_length = this.params.bb_height - this.params.pedal_clearance
      this.params.wheel_radius = this.params.wheel_diameter/2
    }
    else if (isEqArrays(this.latest_defined, ['wheel_diameter', 'pedal_clearance', 'bb_drop', ])) {
      this.params.crank_arm_length = -this.params.bb_drop - this.params.pedal_clearance + this.params.wheel_diameter/2
      this.params.wheel_radius = this.params.wheel_diameter/2
      this.params.bb_height = -this.params.bb_drop + this.params.wheel_diameter/2
    }
    else if (isEqArrays(this.latest_defined, ['wheel_radius', 'crank_arm_length', 'bb_height', ])) {
      this.params.bb_drop = -this.params.bb_height + this.params.wheel_radius
      this.params.pedal_clearance = this.params.bb_height - this.params.crank_arm_length
      this.params.wheel_diameter = 2*this.params.wheel_radius
    }
    else if (isEqArrays(this.latest_defined, ['wheel_radius', 'crank_arm_length', 'pedal_clearance', ])) {
      this.params.bb_drop = -this.params.crank_arm_length - this.params.pedal_clearance + this.params.wheel_radius
      this.params.bb_height = this.params.crank_arm_length + this.params.pedal_clearance
      this.params.wheel_diameter = 2*this.params.wheel_radius
    }
    else if (isEqArrays(this.latest_defined, ['wheel_radius', 'crank_arm_length', 'bb_drop', ])) {
      this.params.wheel_diameter = 2*this.params.wheel_radius
      this.params.pedal_clearance = -this.params.bb_drop - this.params.crank_arm_length + this.params.wheel_radius
      this.params.bb_height = -this.params.bb_drop + this.params.wheel_radius
    }
    else if (isEqArrays(this.latest_defined, ['wheel_radius', 'bb_height', 'pedal_clearance', ])) {
      this.params.bb_drop = -this.params.bb_height + this.params.wheel_radius
      this.params.crank_arm_length = this.params.bb_height - this.params.pedal_clearance
      this.params.wheel_diameter = 2*this.params.wheel_radius
    }
    else if (isEqArrays(this.latest_defined, ['wheel_radius', 'pedal_clearance', 'bb_drop', ])) {
      this.params.wheel_diameter = 2*this.params.wheel_radius
      this.params.crank_arm_length = -this.params.bb_drop - this.params.pedal_clearance + this.params.wheel_radius
      this.params.bb_height = -this.params.bb_drop + this.params.wheel_radius
    }
    else if (isEqArrays(this.latest_defined, ['crank_arm_length', 'bb_height', 'bb_drop', ])) {
      this.params.wheel_diameter = 2*this.params.bb_drop + 2*this.params.bb_height
      this.params.pedal_clearance = this.params.bb_height - this.params.crank_arm_length
      this.params.wheel_radius = this.params.bb_drop + this.params.bb_height
    }
    else if (isEqArrays(this.latest_defined, ['crank_arm_length', 'pedal_clearance', 'bb_drop', ])) {
      this.params.wheel_diameter = 2*this.params.bb_drop + 2*this.params.crank_arm_length + 2*this.params.pedal_clearance
      this.params.wheel_radius = this.params.bb_drop + this.params.crank_arm_length + this.params.pedal_clearance
      this.params.bb_height = this.params.crank_arm_length + this.params.pedal_clearance
    }
    else if (isEqArrays(this.latest_defined, ['bb_height', 'pedal_clearance', 'bb_drop', ])) {
      this.params.wheel_diameter = 2*this.params.bb_drop + 2*this.params.bb_height
      this.params.crank_arm_length = this.params.bb_height - this.params.pedal_clearance
      this.params.wheel_radius = this.params.bb_drop + this.params.bb_height
    }
    
    else if (this.latest_defined.length < this.inputs_required) {
      console.log(this.latest_defined);
      alert('Not enough defined');
      
      for (var name in this.params) {
        if (this.params.hasOwnProperty(name)) {
          if (!inArray(this.latest_defined, name)) {
            this.params[name] = undefined;
          }
        }
      };
    }
    
    else {
      console.log(this.latest_defined);
      alert('Conflicting Inputs');
      
      for (var name in this.params) {
        if (this.params.hasOwnProperty(name)) {
          if (!inArray(this.latest_defined, name)) {
            this.params[name] = undefined;
          }
        }
      };
    }
  };
};
