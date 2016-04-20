from system_soln_funcs import solution_handler, write_soln_func, to_rad
import sympy as sp    

var_names = [
             'seat_tube_length',
             'saddle_height',
             'saddle_extension',
            ]
            
constants = [
            ]

for v in var_names + constants:
    sp.var(v)   

input_names = var_names
            
equations = [
             sp.Eq(saddle_extension, saddle_height - seat_tube_length),
            ]
            
input_vars, soln_vars, solns = solution_handler(var_names=var_names, input_names=input_names, equations=equations)
write_soln_func(var_names=var_names, constant_names=constants, input_vars=input_vars, soln_vars=soln_vars, solns=solns, module_name='seat_tube_eqns', thickness_mod=False)
