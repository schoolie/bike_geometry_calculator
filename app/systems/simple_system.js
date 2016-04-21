
var simple_system = {};

simple_system.init = function() {
  
  this.defined = [];
  this.latest_defined = [];
  
  this.define = function(name) {
    console.log(name);
    this.defined.push(name);
  };
    
  this.inputs_required = 2;      
  
  this.params = {
    a: undefined,
    b: undefined,
    c: undefined,
    d: undefined
  };
  
  this.calculate = function() {
    var l = this.defined.length;
    this.latest_defined = this.defined.slice(l-this.inputs_required,l);
      
    console.log(this.latest_defined);
    if (false) {
    }
    else if (isEqArrays(this.latest_defined, ['b', 'c'])) {
      console.log(this.latest_defined);
      this.params.a = this.params.b - this.params.c;
      this.params.d = this.params.c;
    }
    else if (isEqArrays(this.latest_defined, ['a', 'c'])) {
      console.log(this.latest_defined);
      this.params.b = this.params.a + this.params.c;
      this.params.d = this.params.c;
    }    
    else if (isEqArrays(this.latest_defined, ['b', 'd'])) {
      console.log(this.latest_defined);
      this.params.a = this.params.b - this.params.d;
      this.params.c = this.params.d;
    }
    else if (isEqArrays(this.latest_defined, ['a', 'd'])) {
      console.log(this.latest_defined);
      this.params.b = this.params.a + this.params.d;
      this.params.c = this.params.d;
    }
    else if (isEqArrays(this.latest_defined, ['a', 'b'])) {
      console.log(this.latest_defined);
      this.params.c = this.params.b - this.params.a;
      this.params.d = this.params.c;
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