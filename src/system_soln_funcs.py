
from __future__ import print_function

import numpy as np
import sympy as sp
import warnings
import itertools      
from math import factorial
import multiprocessing

S = sp.Symbol

to_rad = S('pi')/180.0

def solution_handler(var_names=[], input_names=None, bad_combinations=[], required_inputs=[], constants=[], equations=[]):
    soln_vars = []
    input_vars = []
    solns = []
    
    if input_names is None:
        input_names = var_names

    n = len(input_names)
    num_reqd = len(var_names) - len(equations)
    r = num_reqd
        
    comb_count = factorial(n) / factorial(r) / factorial(n-r)
    print('Solving %d Input Combinations' % comb_count)
    
    for soln_var, input_var, soln in [solve_eqns(input) for input in gen_soln_inputs(input_names, 
                                                                                     num_reqd, 
                                                                                     bad_combinations, 
                                                                                     required_inputs, 
                                                                                     var_names, 
                                                                                     equations)]:
        if soln is not None:
            soln_vars.append(soln_var)
            input_vars.append(input_var)
            solns.append(soln)
    
    print('')
    print('%d Valid Solutions Found' % len(input_vars))
            
    return input_vars, soln_vars, solns
    

def gen_soln_inputs(input_names, num_reqd, bad_combinations, required_inputs, var_names, equations):

    for n, input_var in enumerate(itertools.combinations(input_names, num_reqd)):
        
        bad = False
        
        if len(required_inputs) > 0:
            for req in required_inputs:
                if req not in input_var:
                    bad = True

        for bad_comb in bad_combinations:
            if set(bad_comb) <= set(input_var):
                bad = True

        if not bad:
            yield n, input_var, var_names, equations
            
        else:
            yield n, None, var_names, equations
            
        
def solve_eqns(input):
    n = input[0]
    input_var = input[1]
    var_names = input[2]
    equations = input[3]
    
    if input_var is not None:
        
        print('\n', input_var, end='')
        print(' ', end='')    
        
        soln_var = set(var_names) - set(input_var)
        try:
            soln = sp.solve(equations, soln_var, dict=True)
            if len(soln) > 0:
                if max([len(s) for s in soln]) == len(equations):
                    print('%d ' % n, end='')
                    return soln_var, input_var, soln
                else:
                    print('- ', end='')
                    return (None, input_var, None)
            else:
                print('- ', end='')
                return (None, input_var, None)

        except NotImplementedError as e:
            print('- ', end='')
            pass
        except ValueError as e:
            print('- ', end='')
            pass
        return (None, input_var, None)
    else:
        print('. ', end='')
        return (None, input_var, None)
    
        
def input_gen_handler(i, fixed, translations):
  chunksize = 1
  p = multiprocessing.Pool(multiprocessing.cpu_count()-1)
  for f, clutched in p.imap_unordered(gen_clutched_combs, 
                                          gen_multi_inputs(i, fixed, translations), 
                                          chunksize=chunksize):
      yield f, clutched
    
def write_soln_func(var_names=[], constant_names=[], input_vars=[], soln_vars=[], solns=[], module_name='temp_equations', thickness_mod=False):
    with open('calc_func_base.py', 'rb') as base_file:
        with open('equation_systems\%s.py' % module_name, 'wb') as new_file:

            for line in base_file.read():
                new_file.write(line)
                    
            print('\n    if False:\n        pass', file=new_file)

            for input_var, soln_var, soln in zip(input_vars, soln_vars, solns):
                            
                if thickness_mod:
                    
                    conversion_names = ['diameter_over_pins_1', 'diameter_over_pins_2', 'op_trans_tooth_thickness_1', 'op_trans_tooth_thickness_2']
                    input_var = list(input_var)
                    
                    # Replace variables in input set if necessary
                    try:
                        input_var.remove('op_trans_tooth_thickness_1')
                        input_var.append('diameter_over_pins_1')

                    except ValueError:
                        pass
                    
                    try:
                        input_var.remove('op_trans_tooth_thickness_2')       
                        input_var.append('diameter_over_pins_2')
                    except ValueError:
                        pass
                    
                    # Write if statement
                    print('\n    elif input_var_names == %r:' % set(input_var,), file=new_file)


                
                else:
                    # print('no conv')
                    conversion_names = []
                    print('\n    elif input_var_names == %r:' % set(input_var,), file=new_file)
                        
                        
                
                # Write system equations
                for s in soln:
                    
                    # Calculate corresponding tooth thickness from diameter over pins when given
                    if 'diameter_over_pins_1' in input_var:
                        print('        op_trans_tooth_thickness_1 = calc_tooth_thick_from_pin_dimension(N_1, base_helix_angle, pin_diameter_1, base_diameter_1, diameter_over_pins_1, op_pitch_diameter_1, op_trans_pressure_angle, sign=sign_1)', file=new_file)
                    if 'diameter_over_pins_2' in input_var:
                        print('        op_trans_tooth_thickness_2 = calc_tooth_thick_from_pin_dimension(N_2, base_helix_angle, pin_diameter_2, base_diameter_2, diameter_over_pins_2, op_pitch_diameter_2, op_trans_pressure_angle, sign=sign_2)', file=new_file)

                    print('', file=new_file) 
                
                    # Print formulas from system soln
                    for key, val in s.iteritems():
                        formula = str(val).replace('0.00555555555555556', '1.0/180.0').replace('Abs', 'abs').replace('asin', 'arcsin').replace('acos', 'arccos').replace('atan', 'arctan').replace('I', '1j')
                        
                        if str(key) not in ['diameter_over_pins_1', 'diameter_over_pins_2']: 
                            print("        %s = %s" % (key, formula), file=new_file)
    
                    
                    # Print pin diameter calcs
                    if thickness_mod:
                        print('', file=new_file) 
                        print('        diameter_over_pins_1 = calc_diameter_over_pins(N_1, base_helix_angle, pin_diameter_1, base_diameter_1, op_trans_tooth_thickness_1, op_pitch_diameter_1, op_trans_pressure_angle, sign=sign_1)', file=new_file)
                        print('        diameter_over_pins_2 = calc_diameter_over_pins(N_2, base_helix_angle, pin_diameter_2, base_diameter_2, op_trans_tooth_thickness_2, op_pitch_diameter_2, op_trans_pressure_angle, sign=sign_2)', file=new_file)
                        
                        
                    print('\n        outputs.append({', file=new_file)
                    for key in set(s.keys()).union(set(conversion_names)):
                        print ("            '%s': %s," % (key, key), file=new_file)
                    print('        })\n', file=new_file)
                    
            print('    return outputs', file=new_file)
            
            print('\n\n', file=new_file)
            print('valid_input_sets = [', file=new_file)
            for input_var in input_vars:
                
                input_var = list(input_var)
                    
                # Replace variables in input set if necessary
                try:
                    input_var.remove('op_trans_tooth_thickness_1')
                    input_var.append('diameter_over_pins_1')

                except ValueError:
                    pass

                try:
                    input_var.remove('op_trans_tooth_thickness_2')       
                    input_var.append('diameter_over_pins_2')
                except ValueError:
                    pass
                
                print('    %r,' % set(input_var), file=new_file)
            print(']', file=new_file)
            
            print('', file=new_file)
            print('var_names = [', file=new_file)
            for v in var_names:
                print("    '%s'," % v, file=new_file)
            print(']', file=new_file)            
            
            print('', file=new_file)
            print('constant_names = [', file=new_file)
            for c in constant_names:
                print("    '%s'," % c, file=new_file)
            print(']', file=new_file)
            
    print('equation_systems\%s.py written' % module_name)

def write_soln_func_js(var_names=[], constant_names=[], input_vars=[], soln_vars=[], solns=[], module_name='temp_equations', thickness_mod=False):
    with open('equation_systems\%s.js' % module_name, 'wb') as new_file:
        print("var {} = {{}};".format(module_name), file=new_file)
        print("", file=new_file)
        print("{}.init = function() {{".format(module_name), file=new_file)
        print("  this.defined = [];", file=new_file)
        print("  this.latest_defined = [];", file=new_file)
        print("", file=new_file)
        print("  this.define = function(name) {", file=new_file)
        print("    this.defined.push(name);", file=new_file)
        print("  };", file=new_file)
        print("", file=new_file)
        print("  this.inputs_required = {};".format(len(soln_vars[0])), file=new_file)  
        print("", file=new_file)
        
        print("  this.params = {", file=new_file)
        for var in var_names:
            print("    {}: undefined,".format(var), file=new_file)
        print("  };", file=new_file)
            
        print("", file=new_file)
        print("  this.calculate = function() {", file=new_file)
        print("    var l = this.defined.length;", file=new_file)
        print("    this.latest_defined = this.defined.slice(l-this.inputs_required,l);", file=new_file)
                  

        print("", file=new_file)
        print("    if (false) {", file=new_file)
        print("    }", file=new_file)


        for input_var, soln_var, soln in zip(input_vars, soln_vars, solns):
            soln = soln[0]
            
            print("    else if (isEqArrays(this.latest_defined, [", file=new_file, end='')
            for var in input_var:
                print("'{}', ".format(var), file=new_file, end='')
            print("])) {", file=new_file)
            
            # print("      console.log(this.latest_defined);", file=new_file)
            for var in soln.keys():
                print('      ' + print_equation(var, soln, var_names), file=new_file)
            
            print("    }", file=new_file)
        end = """    
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
};"""
        print(end, file=new_file)
        
    print('equation_systems\%s.js written' % module_name)

def print_equation(var, soln, var_names):
    equation = soln[var]
    result = '{var} = {equation}'.format(var=var, equation=equation)
    for name in var_names:
        result = result.replace(name, 'this.params.{}'.format(name))
    return result