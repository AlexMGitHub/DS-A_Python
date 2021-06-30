#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 3 exercises.

###############################################################################
# test_chapter3.py
#
# Revision:     1.00
# Date:         6/26/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 3 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Related third party imports
# import pytest
import numpy as np

# Local application/library specific imports
import dsa.chapter3_exercises as chap3


# %% Reinforcement Exercises
def test_graph_log_scale():
    """Solution to exercise R-3.1.

    Graph the functions 8n, 4n log n, 2n 2 , n 3 , and 2 n using a
    logarithmic scale for the x- and y-axes; that is, if the function value
    f (n) is y, plot this as a point with x-coordinate at log n and
    y-coordinate at log y.
    """
    assert chap3.graph_log_scale(2**8)


def test_r_3p2():
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
    def algorithm_a(n):
        return 8 * n * np.log2(n)

    def algorithm_b(n):
        return 2 * n ** 2

    n0 = chap3.r_3p2()
    assert algorithm_a(n0) == algorithm_b(n0)
    assert algorithm_a(n0+1) < algorithm_b(n0+1)
    assert algorithm_a(n0-1) > algorithm_b(n0-1)


def test_r_3p3():
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
    def algorithm_a(n):
        return 40 * n ** 2

    def algorithm_b(n):
        return 2 * n ** 3

    n0 = chap3.r_3p3()
    assert algorithm_a(n0) == algorithm_b(n0)
    assert algorithm_a(n0+1) < algorithm_b(n0+1)
    assert algorithm_a(n0-1) > algorithm_b(n0-1)


def test_log_log_scale():
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
    assert chap3.log_log_scale()


def test_sum_of_even_nums():
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
    n_list = [2, 10, 25, 100]
    for n in n_list:
        assert chap3.sum_of_even_nums(n) == sum(range(0, 2*n+1, 2))
