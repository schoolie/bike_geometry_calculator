from system_soln_funcs import solution_handler, write_soln_func
import sympy as sp    

var_names = [
             'wheel_diameter',
             'wheel_radius',
             'crank_arm_length',
             'bb_height',
             'pedal_clearance',
            ]
            
constants = [
             'bb_drop'
            ]

for v in var_names + constants:
    sp.var(v)   

input_names = var_names
            
equations = [
             sp.Eq(wheel_diameter, wheel_radius * 2),
             sp.Eq(bb_height, wheel_radius - bb_drop),
             sp.Eq(pedal_clearance, bb_height - crank_arm_length),
            ]
            
input_vars, soln_vars, solns = solution_handler(var_names=var_names, input_names=input_names, equations=equations)
            
