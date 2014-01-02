#!usr/bin/env python
# -*- coding: utf-8 -*-

""" Utility functions for exploration of the Python language
to write up on my blog
"""

import timeit as timeit_

def timeit(code_string, setup='pass'):
    """ Implementation of timeit that replicates behaviour of the
    'python -mtimeit' command, to make it available in the interactive 
    prompt and saved modules. 
    """
    USEC_PER_SEC = 10**6


    number_of_loops = 1
    total_iteration_time = 0
    while total_iteration_time < 0.2:
        number_of_loops *= 10

        time_result_list = timeit_.repeat(stmt=code_string,
                setup=setup, number=number_of_loops)

        total_iteration_time = sum(time_result_list)

        best_time_per_loop = (min(time_result_list) * USEC_PER_SEC 
                                                    * 1./number_of_loops)

    if best_time_per_loop  >= 1000:
        best_time_per_loop  /= 1000
        representation = 'ms'
    elif best_time_per_loop  < 1:
        best_time_per_loop  *= 1000
        representation = 'ns'
    else:
        representation = 'us'

    preformat_string = '{0:10d} loops, best of 3: {1:5.1f} {2} per loop' 
    print preformat_string.format(number_of_loops,
                                  best_time_per_loop,
                                  representation)

