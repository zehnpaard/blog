#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Template for writing code that tests running time and
prints the results in a readable format.
"""

from blog_utils import timeit



def create_code_strings():
    """ Create list of text strings that are the snippets of code
    to be run against timeit
    """

    code_strings = []

    code_strings.append(
"""\
for x in xrange(10):
    1 + 1
""")

    code_strings.append(
"""\
1 + 1
""")



    return code_strings


def print_timeit(code_strings):
    """ Print the code and the timeit output, with some embellishments
    """
    print
    for code in code_strings:
        print code,
        print '-'*50
        timeit(code)
        print '-'*50
        print


def main():

    code_strings = create_code_strings()

    print_timeit(code_strings)


if __name__ == '__main__':
    main()


