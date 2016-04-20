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
    