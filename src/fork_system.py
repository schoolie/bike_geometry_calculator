from system_soln_funcs import solution_handler, write_soln_func, to_rad
import sympy as sp    

var_names = [
             'head_tube_angle',
             'fork_a_c',
             'fork_offset',
             'fork_length',
             'ground_trail',
             'mech_trail',
             'crown_to_steering_axis_intersection'            
            ]
            
constants = [
             'wheel_radius'
            ]

for v in var_names + constants:
    sp.var(v)   

input_names = [
               'head_tube_angle',
               'fork_a_c',
               'fork_offset',
               'fork_length',
               'ground_trail',
               'mech_trail',
            ]
            
bad_combinations = [['fork_a_c', 'fork_offset', 'fork_length']]
equations = [
             sp.Eq(fork_length, (fork_a_c**2 - fork_offset**2)**0.5),  
             sp.Eq(ground_trail, (wheel_radius*sp.cos(head_tube_angle*to_rad)-fork_offset)/sp.sin(head_tube_angle*to_rad)),
             sp.Eq(mech_trail, sp.cos(head_tube_angle*to_rad)*wheel_radius - fork_offset),
             sp.Eq(crown_to_steering_axis_intersection, 
                   fork_length+fork_offset*sp.tan(head_tube_angle*to_rad) + ground_trail/sp.cos(head_tube_angle*to_rad)),
            ]
            
input_vars, soln_vars, solns = solution_handler(var_names=var_names, input_names=input_names, bad_combinations=bad_combinations, equations=equations)
            
