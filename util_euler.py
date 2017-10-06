#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#
#  Utility functions used to solve some project Euler puzzles
#
#


def MeasureTime(function):
    """ Simple decorator to measure execution time of a function. """
    from functools import wraps

    @wraps(function)
    def decorated_function(*args, **kwargs):
        import time

        start = time.time()
        output = function(*args, **kwargs)
        print "{0:.5f} ms".format(1000 * (time.time() - start))

        return output

    return decorated_function
