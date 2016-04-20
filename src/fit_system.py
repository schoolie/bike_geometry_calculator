from system_soln_funcs import solution_handler, write_soln_func, to_rad
import sympy as sp    

var_names = [
             'stack',
             'reach',
             'ht_top_to_ground',
             'seat_tube_angle',
             'head_tube_length',
             'lower_hs_stack',
             'effective_top_tube',
             # 'seat_tube_length',
             # 'saddle_height',
             # 'saddle_extension',
            ]
            
constants = [
             'bb_height',
             'head_tube_angle',
             'crown_to_steering_axis_intersection',
             'front_wheelbase',
             'ground_trail'
            ]

for v in var_names + constants:
    sp.var(v)   

input_names = var_names
            
equations = [
             sp.Eq(stack, (crown_to_steering_axis_intersection + head_tube_length + lower_hs_stack)*sp.sin(head_tube_angle*to_rad)-bb_height),
             sp.Eq(reach, (front_wheelbase+ground_trail)-(crown_to_steering_axis_intersection + head_tube_angle + lower_hs_stack)*sp.cos(head_tube_angle*to_rad)),
             sp.Eq(ht_top_to_ground, stack+bb_height),
             sp.Eq(effective_top_tube, stack * sp.tan((90-seat_tube_angle)*to_rad) + reach),
             # sp.Eq(saddle_extension, saddle_height - seat_tube_length),
            ]
            
input_vars, soln_vars, solns = solution_handler(var_names=var_names, input_names=input_names, equations=equations)
            
