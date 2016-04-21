from numpy import cos, sin, tan, pi, arcsin, arccos, arctan, sqrt, exp
from func import calc_diameter_over_pins, calc_tooth_thick_from_pin_dimension

def calc(constants=None, inputs=None):    

    # Add input variables to namespace to simplify equation definition
    for key, val in inputs.iteritems():
        exec '%s = float(%r)' % (key, val)

    for key, val in constants.iteritems():
        exec '%s = float(%r)' % (key, val)

    outputs = []
    
    input_var_names = set(inputs.keys())    
    
    if False:
        pass

    elif input_var_names == set(['crank_arm_length', 'bb_height', 'wheel_diameter']):

        bb_drop = -bb_height + wheel_diameter/2
        pedal_clearance = bb_height - crank_arm_length
        wheel_radius = wheel_diameter/2

        outputs.append({
            'bb_drop': bb_drop,
            'pedal_clearance': pedal_clearance,
            'wheel_radius': wheel_radius,
        })


    elif input_var_names == set(['crank_arm_length', 'pedal_clearance', 'wheel_diameter']):

        bb_drop = -crank_arm_length - pedal_clearance + wheel_diameter/2
        wheel_radius = wheel_diameter/2
        bb_height = crank_arm_length + pedal_clearance

        outputs.append({
            'bb_drop': bb_drop,
            'wheel_radius': wheel_radius,
            'bb_height': bb_height,
        })


    elif input_var_names == set(['crank_arm_length', 'bb_drop', 'wheel_diameter']):

        pedal_clearance = -bb_drop - crank_arm_length + wheel_diameter/2
        wheel_radius = wheel_diameter/2
        bb_height = -bb_drop + wheel_diameter/2

        outputs.append({
            'pedal_clearance': pedal_clearance,
            'wheel_radius': wheel_radius,
            'bb_height': bb_height,
        })


    elif input_var_names == set(['bb_height', 'pedal_clearance', 'wheel_diameter']):

        bb_drop = -bb_height + wheel_diameter/2
        crank_arm_length = bb_height - pedal_clearance
        wheel_radius = wheel_diameter/2

        outputs.append({
            'bb_drop': bb_drop,
            'crank_arm_length': crank_arm_length,
            'wheel_radius': wheel_radius,
        })


    elif input_var_names == set(['bb_drop', 'pedal_clearance', 'wheel_diameter']):

        crank_arm_length = -bb_drop - pedal_clearance + wheel_diameter/2
        wheel_radius = wheel_diameter/2
        bb_height = -bb_drop + wheel_diameter/2

        outputs.append({
            'crank_arm_length': crank_arm_length,
            'wheel_radius': wheel_radius,
            'bb_height': bb_height,
        })


    elif input_var_names == set(['crank_arm_length', 'bb_height', 'wheel_radius']):

        bb_drop = -bb_height + wheel_radius
        pedal_clearance = bb_height - crank_arm_length
        wheel_diameter = 2*wheel_radius

        outputs.append({
            'bb_drop': bb_drop,
            'pedal_clearance': pedal_clearance,
            'wheel_diameter': wheel_diameter,
        })


    elif input_var_names == set(['crank_arm_length', 'pedal_clearance', 'wheel_radius']):

        bb_drop = -crank_arm_length - pedal_clearance + wheel_radius
        bb_height = crank_arm_length + pedal_clearance
        wheel_diameter = 2*wheel_radius

        outputs.append({
            'bb_drop': bb_drop,
            'bb_height': bb_height,
            'wheel_diameter': wheel_diameter,
        })


    elif input_var_names == set(['crank_arm_length', 'wheel_radius', 'bb_drop']):

        wheel_diameter = 2*wheel_radius
        pedal_clearance = -bb_drop - crank_arm_length + wheel_radius
        bb_height = -bb_drop + wheel_radius

        outputs.append({
            'wheel_diameter': wheel_diameter,
            'pedal_clearance': pedal_clearance,
            'bb_height': bb_height,
        })


    elif input_var_names == set(['bb_height', 'pedal_clearance', 'wheel_radius']):

        bb_drop = -bb_height + wheel_radius
        crank_arm_length = bb_height - pedal_clearance
        wheel_diameter = 2*wheel_radius

        outputs.append({
            'bb_drop': bb_drop,
            'crank_arm_length': crank_arm_length,
            'wheel_diameter': wheel_diameter,
        })


    elif input_var_names == set(['pedal_clearance', 'wheel_radius', 'bb_drop']):

        wheel_diameter = 2*wheel_radius
        crank_arm_length = -bb_drop - pedal_clearance + wheel_radius
        bb_height = -bb_drop + wheel_radius

        outputs.append({
            'wheel_diameter': wheel_diameter,
            'crank_arm_length': crank_arm_length,
            'bb_height': bb_height,
        })


    elif input_var_names == set(['crank_arm_length', 'bb_height', 'bb_drop']):

        wheel_diameter = 2*bb_drop + 2*bb_height
        pedal_clearance = bb_height - crank_arm_length
        wheel_radius = bb_drop + bb_height

        outputs.append({
            'wheel_diameter': wheel_diameter,
            'pedal_clearance': pedal_clearance,
            'wheel_radius': wheel_radius,
        })


    elif input_var_names == set(['crank_arm_length', 'pedal_clearance', 'bb_drop']):

        wheel_diameter = 2*bb_drop + 2*crank_arm_length + 2*pedal_clearance
        wheel_radius = bb_drop + crank_arm_length + pedal_clearance
        bb_height = crank_arm_length + pedal_clearance

        outputs.append({
            'wheel_diameter': wheel_diameter,
            'wheel_radius': wheel_radius,
            'bb_height': bb_height,
        })


    elif input_var_names == set(['bb_height', 'pedal_clearance', 'bb_drop']):

        wheel_diameter = 2*bb_drop + 2*bb_height
        crank_arm_length = bb_height - pedal_clearance
        wheel_radius = bb_drop + bb_height

        outputs.append({
            'wheel_diameter': wheel_diameter,
            'crank_arm_length': crank_arm_length,
            'wheel_radius': wheel_radius,
        })

    return outputs



valid_input_sets = [
    set(['crank_arm_length', 'bb_height', 'wheel_diameter']),
    set(['crank_arm_length', 'pedal_clearance', 'wheel_diameter']),
    set(['crank_arm_length', 'bb_drop', 'wheel_diameter']),
    set(['bb_height', 'pedal_clearance', 'wheel_diameter']),
    set(['bb_drop', 'pedal_clearance', 'wheel_diameter']),
    set(['crank_arm_length', 'bb_height', 'wheel_radius']),
    set(['crank_arm_length', 'pedal_clearance', 'wheel_radius']),
    set(['crank_arm_length', 'wheel_radius', 'bb_drop']),
    set(['bb_height', 'pedal_clearance', 'wheel_radius']),
    set(['pedal_clearance', 'wheel_radius', 'bb_drop']),
    set(['crank_arm_length', 'bb_height', 'bb_drop']),
    set(['crank_arm_length', 'pedal_clearance', 'bb_drop']),
    set(['bb_height', 'pedal_clearance', 'bb_drop']),
]

var_names = [
    'wheel_diameter',
    'wheel_radius',
    'crank_arm_length',
    'bb_height',
    'pedal_clearance',
    'bb_drop',
]

constant_names = [
]
