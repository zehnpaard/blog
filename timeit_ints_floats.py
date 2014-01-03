#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tests execution of various operations on integers and floats
"""

from blog_utils import timeit, print_timeit, print_timeit_table



def main():
    """ Create list of text strings that are the snippets of code
    to be run against timeit
    """

    base_string = "{0} {1} {2}"
    
    numbers = (1, 8, 13, int(2**31-1), int(2**31))
    float_nums = [float(n) for n in numbers]
    operators = ('+', '-', '*', '/', '%', '>', '<', '>=', '==')
    code_strings = [base_string.format(n, op, m) for n in numbers
                                                 for op in operators
                                                 for m in numbers]

    code_strings += [base_string.format(n, op, m) for n in float_nums
                                                  for op in operators
                                                  for m in float_nums]

    code_strings += [base_string.format(n, op, m) for n in float_nums
                                                  for op in operators
                                                  for m in numbers]

    exponent_strings = ('{0}**{1}', 'pow({0},{1})', '{0}**-{1}', 'pow({0},-{1})')
    code_strings += [exp_string.format(n, m) for exp_string in exponent_strings
                                             for n in numbers
                                             for m in numbers[:-2]]

    code_strings += ['float({0})'.format(n) for n in numbers]
    code_strings += ['{0}*1.'.format(n) for n in numbers]
    code_strings += ['int({0})'.format(n) for n in float_nums]


    print_timeit_table(code_strings)


if __name__ == '__main__':
    main()


