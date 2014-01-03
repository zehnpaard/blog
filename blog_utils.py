#!usr/bin/env python
# -*- coding: utf-8 -*-

""" Utility functions for exploration of the Python language
to write up on my blog
"""

import timeit as timeit_



def timeit(code_string, setup='pass', output='print'):
    """ Implementation of timeit that replicates behaviour of the
    'python -mtimeit' command, to make it available in the interactive 
    prompt and saved modules. 
    """
    assert output in ('print', 'return')


    USEC_PER_SEC = 10**6


    """
    Get the 'best of three' average per loop in microseconds
    The number of loops starts with 1, and goes up by an order
    of magnitude until the time taken to compute all the loops 
    3 times becomes greater than 200 milliseconds
    """
    number_of_loops = 1
    total_iteration_time = 0

    while total_iteration_time < 0.2:
        number_of_loops *= 10
        time_result_list = timeit_.repeat(stmt=code_string,
                setup=setup, number=number_of_loops)
        total_iteration_time = sum(time_result_list)

    best_time_per_loop = (min(time_result_list) * USEC_PER_SEC 
                                                * 1./number_of_loops)
    representation = 'us'

    """
    Update time and the string holding representation if 
    the time is greater than 1 millisecond or smaller 
    than 1000 nanoseconds
    """
    if best_time_per_loop  >= 1000:
        best_time_per_loop  /= 1000
        representation = 'ms'
    elif best_time_per_loop  < 1:
        best_time_per_loop  *= 1000
        representation = 'ns'


    # Print or return tuple based on the 'output' flag
    if output == 'print':
        preformat_string = '{0:10d} loops, best of 3: {1:5.1f} {2} per loop' 
        print preformat_string.format(number_of_loops,
                                      best_time_per_loop,
                                      representation)
    elif output == 'return':
        return (number_of_loops, best_time_per_loop, representation)


def print_timeit(code_strings):
    """ Take an iterable with code strings.  For each code string, print 
    the code string and the timeit output, with some embellishments
    """
    print
    for code in code_strings:
        print code
        print '-'*50
        timeit(code)
        print '-'*50
        print
        

def print_timeit_table(code_strings):
    """ Take an iterable with code strings. Print a summary table that 
    displays the code and timeit outputs.
    """
    print '{0:40}:{1:>7}'.format('Code', 'Time Taken')
    print '-'*51
    for code in code_strings:
        loops, time, representation = timeit(code, output='return')
        print '{0:40}:{1:7.1f}{2:>3}'.format(code, time, representation)
