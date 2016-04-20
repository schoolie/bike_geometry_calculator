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

    elif input_var_names == set(['saddle_height', 'seat_tube_length']):

        saddle_extension = saddle_height - seat_tube_length

        outputs.append({
            'saddle_extension': saddle_extension,
        })


    elif input_var_names == set(['saddle_extension', 'seat_tube_length']):

        saddle_height = saddle_extension + seat_tube_length

        outputs.append({
            'saddle_height': saddle_height,
        })


    elif input_var_names == set(['saddle_height', 'saddle_extension']):

        seat_tube_length = -saddle_extension + saddle_height

        outputs.append({
            'seat_tube_length': seat_tube_length,
        })

    return outputs



valid_input_sets = [
    set(['saddle_height', 'seat_tube_length']),
    set(['saddle_extension', 'seat_tube_length']),
    set(['saddle_height', 'saddle_extension']),
]

var_names = [
    'seat_tube_length',
    'saddle_height',
    'saddle_extension',
]

constant_names = [
]
