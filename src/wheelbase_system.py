from system_soln_funcs import solution_handler, write_soln_func
import sympy as sp    
var_names = [
             'front_center',
             'chainstay_length',
             'bb_drop',
             'wheelbase',
             'front_wheelbase',
             'rear_wheelbase'
            ]
for v in var_names:
    sp.var(v)
input_names = [
               'front_center',
               'chainstay_length',
               'bb_drop',
               'wheelbase',
              ]
equations = [
             sp.Eq(wheelbase, front_wheelbase + rear_wheelbase),
             sp.Eq(front_wheelbase, (front_center**2 - bb_drop**2)**0.5),
             sp.Eq(rear_wheelbase, (chainstay_length**2 - bb_drop**2)**0.5),
            ]
                             
input_vars, soln_vars, solns = solution_handler(var_names=var_names, input_names=input_names, equations=equations)
# write_soln_func(var_names=var_names, constant_names=constants, input_vars=input_vars, soln_vars=soln_vars, solns=solns, module_name='tooth_height_system')