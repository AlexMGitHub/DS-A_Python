#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 3 exercises.

###############################################################################
# chapter3_exercises.py
#
# Revision:     1.00
# Date:         6/26/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 3 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports
import numpy as np
import matplotlib.pyplot as plt

# Local application/library specific imports


# %% Reinforcement Exercises
def graph_log_scale(n_max, num_pts=100):
    """Solution to exercise R-3.1.

    Graph the functions 8n, 4nlog n, 2n^2 , n^3 , and 2^n using a
    logarithmic scale for the x- and y-axes; that is, if the function value
    f (n) is y, plot this as a point with x-coordinate at log n and
    y-coordinate at log y.
    """
    n = np.linspace(2, n_max, num=num_pts, endpoint=True)
    functions = [8*n, 4*n*np.log2(n), 2*n**2, n**3, 2**n]
    labels = ['$8n$', '$4nlog_2n$', '$2n^2$', '$n^3$', '$2^n$']
    for function, label in zip(functions, labels):
        plt.loglog(n, function, base=10, label=label)
    plt.xlabel('$n$')
    plt.ylabel('$f(n)$')
    plt.ylim((1, 10 ** 8))
    plt.legend()
    plt.grid()
    return True


def r_3p2():
    """Solution to exercise R-3.2.

    The number of operations executed by algorithms A and B is 8n*logn and
    2n^2, respectively. Determine n_0 such that A is better than B for n ≥ n_0.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    8n*log2(n)  <= 2n^2     for every integer n >= n_0
    4*log2(n)   <= n

    I can solve this equation by inspection, recognizing that log2(16) = 4:

    4*log2(16)  == 16
    4*4         == 16

    Therefore algorithm A is O(B) when n_0 >= 16.
    """
    return 16


def r_3p3():
    """Solution to exercise R-3.3.

    The number of operations executed by algorithms A and B is 40n^2 and
    2n^3, respectively. Determine n_0 such that A is better than B for n ≥ n_0.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    40n^2   <= 2n^3     for every integer n >= n_0
    20      <= n

    Therefore algorithm A is O(B) when n_0 >= 20.
    """
    return 20


def log_log_scale():
    """Solution to exercise R-3.5.

    Explain why the plot of the function n^c is a straight line with slope c
    on a log-log scale.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The log-log plot takes the log of both x and f(x), such that the x-axis
    will be log(n) and the y-axis will be log(n^c).

    From rule 3 of Proposition 3.1:
    logb(a^c) = c * logb(a)

    Therefore:
    log(n^c) = c * log(n)

    And the log-log plot will have a slope (rise over run) of:
    c * log(n) / log(n)

    Which results in a constant, straight line slope of c.
    """
    return True


def sum_of_even_nums(n):
    """Solution to exercise R-3.6.

    What is the sum of all the even numbers from 0 to 2n, for any positive
    integer n?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    We know from Proposition 3.3 that for any integer n >= 1, the sum of the
    first n integers is n * (n + 1) / 2.

    However, because only even numbers are being summed, this is an arithmetic
    progression with a common difference of 2.  The sum of a finite arithmetic
    progression is given by:

    n * (a_1 + a_n) / 2     Where a_1 is the first term and a_n is the nth term

    If we are summing the first 2n even numbers, then n is the number of even
    terms, a_1 is 2, and a_n is 2n.  Therefore the solution is:

    n * (2 + 2*n) / 2
    """
    return n * (2 + 2*n) / 2
