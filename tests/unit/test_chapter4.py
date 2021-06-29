#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 4 exercises.

###############################################################################
# test_chapter4.py
#
# Revision:     1.00
# Date:         6/27/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 4 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports
import sys
import os
from timeit import timeit

# Related third party imports
import numpy as np
import pytest

# Local application/library specific imports
import dsa.chapter4_exercises as chap4


# %% Reinforcement Exercises
def test_harmonic_number():
    """Solution to exercise R-4.6.

    Describe a recursive function for computing the nth Harmonic number.
    """
    nums = [8, 27, 32, 105, 42, 16, 3]
    for num in nums:
        harmonic = 0
        for i in range(1, num+1):
            harmonic += 1 / i
        assert chap4.harmonic_number(num) == harmonic


def test_str_to_int():
    """Solution to exercise R-4.7.

    Describe a recursive function for converting a string of digits into the
    integer it represents. For example, "13531" represents the integer 13,531.
    """
    strings = ['13531', '888', '1', '0', '29', '67', '999', '75']
    for string in strings:
        assert chap4.str_to_int(string) == int(string)


# %% Creativity Exercises
def test_find_min_max():
    """Solution to exercise C-4.9.

    Write a short recursive Python function that finds the minimum and
    maximum values in a sequence without using any loops.
    """
    np.random.seed = 111
    data1 = list(np.random.randint(0, 1000, size=100))
    data2 = tuple(np.random.randint(0, 1000, size=50))
    data3 = list(np.random.randint(0, 1000, size=100))
    assert chap4.find_min_max(data1) == (min(data1), max(data1))
    assert chap4.find_min_max(data2) == (min(data2), max(data2))
    assert chap4.find_min_max(data3) == (min(data3), max(data3))


def test_recursive_log():
    """Solution to exercise C-4.10.

    Describe a recursive algorithm to compute the integer part of the base-two
    logarithm of n using only addition and integer division.
    """
    nums = [32, 28, 104, 128, 167, 1003, 8, 12, 2]
    for num in nums:
        assert chap4.recursive_log(num) == int(np.log2(num))


@pytest.mark.slow
def test_recursive_unique():
    """Solution to exercise C-4.11.

    Describe an efficient recursive function for solving the element
    uniqueness problem, which runs in time that is at most O(n^2) in the
    worst case without using sorting.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The nonrecursive part of each call uses O(1) time, so the overall running
    time will be proportional to the total number of recursive invocations.
    However, unlike the "bad" recursion example in the text, my function does
    not make more than one recursive call per invocation.  It is a linear
    recursion algorithm

    The algorithm works by decrementing the stop index until it reaches the
    start index.  Once that happens, the stop index is reset to the end of the
    sequence and the start index is incremented by 1.

    The first recursion call in the conditional statements only executes if
    the stop index hasn't reached the start index yet.  The second recursion
    call only occurs if the start index hasn't reached the end of the sequence
    yet.  Both calls are placed in an "elif" statement that makes them mutually
    exclusive.  In other words, a maximum of one recursive call per invocation.

    Based on the above description, it's clear that the algorithm is worst
    case O(n^2).  It's equivalent to a nested loop with n outer iterations and
    (n-1), (n-2) ... 1 inner iterations.  This is well-known to be O(n^2).

    I used timeit to verify that the execution time of my algorithm grows
    approximately as n^2.
    """
    np.random.seed = 11
    # Lists containing only unique elements
    unique1 = list(range(30))
    unique2 = unique1.copy()
    np.random.shuffle(unique2)
    # Lists with varying number of duplicates
    not_unique1 = list(np.random.randint(0, 20, size=30))
    not_unique2 = list(np.random.randint(0, 29, size=30))
    not_unique3 = unique1.copy()
    not_unique3[15] = 23  # One duplicate
    # Test functionality
    assert chap4.recursive_unique(unique1)
    assert chap4.recursive_unique(unique2)
    assert not chap4.recursive_unique(not_unique1)
    assert not chap4.recursive_unique(not_unique2)
    assert not chap4.recursive_unique(not_unique3)
    # Test execution time to verify O(n^2)
    n1 = 20
    n2 = 40
    recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(10000)  # Temporarily increase recursion limit
    growth = (n2 / n1) ** 2  # Expected time ratio for O(n^2) algorithm
    unique30 = list(range(n1))  # n = 30 elements
    unique40 = list(range(n2))  # n = 90 elements
    time1 = timeit(lambda: chap4.recursive_unique(unique30), number=10000)
    time2 = timeit(lambda: chap4.recursive_unique(unique40), number=10000)
    assert (0.8*growth) <= time2/time1 <= (1.2*growth)
    sys.setrecursionlimit(recursion_limit)  # Revert to original limit


def test_integer_product():
    """Solution to exercise C-4.12.

    Give a recursive algorithm to compute the product of two positive integers,
    m and n, using only addition and subtraction.
    """
    assert chap4.integer_product(3, 4) == 12
    assert chap4.integer_product(5, 5) == 25
    assert chap4.integer_product(1, 1) == 1
    assert chap4.integer_product(2, 1) == 2


@pytest.mark.parametrize('n_disks', [4, 5, 6])
def test_towers_of_hanoi(n_disks):
    """Solution to exercise C-4.14.

    In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
    b, and c, sticking out of it. On peg a is a stack of n disks, each larger
    than the next, so that the smallest is on the top and the largest is on the
    bottom.  The puzzle is to move all the disks from peg a to peg c, moving
    one disk at a time, so that we never place a larger disk on top of a
    smaller one.
    See Figure 4.15 for an example of the case n = 4. Describe a recursive
    algorithm for solving the Towers of Hanoi puzzle for arbitrary n.
    """
    tower = chap4.towers_of_hanoi(n_disks)
    assert len(tower) == n_disks
    assert tower == list(range(n_disks, 0, -1))


def test_all_subsets():
    """Solution to exercise C-4.15.

    Write a recursive function that will output all the subsets of a set of n
    elements (without repeating any subsets).

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I've made the following assumptions:
        1. The input is a set of unique numbers
        2. The set itself is considered a subset (not a proper subset)
        3. The null (empty) set is considered a subset
    """
    set1 = ['a', 'b', 'c']
    result = chap4.all_subsets(set1)
    expected_results = [
        [],
        ['a'],
        ['b'],
        ['c'],
        ['a', 'b'],
        ['b', 'c'],
        ['a', 'c'],
        set1
        ]
    assert len(result) == 8
    for subset in expected_results:
        assert subset in result


def test_reverse_string():
    """Solution to exercise C-4.16.

    Write a short recursive Python function that takes a character string s and
    outputs its reverse. For example, the reverse of "pots&pans" would be
    "snap&stop".
    """
    string1 = "pots&pans"
    string2 = "abc"
    assert chap4.reverse_string(string1) == "snap&stop"
    assert chap4.reverse_string(string2) == "cba"


def test_is_palindrome():
    """Solution to exercise C-4.17.

    Write a short recursive Python function that determines if a string s is a
    palindrome, that is, it is equal to its reverse. For example, "racecar"
    and "gohangasalamiimalasagnahog" are palindromes.
    """
    assert chap4.is_palindrome("gohangasalamiimalasagnahog")
    assert chap4.is_palindrome("racecar")
    assert not chap4.is_palindrome("test")
    assert not chap4.is_palindrome("abcab")


def test_more_vowels():
    """Solution to exercise C-4.18.

    Use recursion to write a Python function for determining if a string s has
    more vowels than consonants.
    """
    assert not chap4.more_vowels('abc')
    assert not chap4.more_vowels('running')
    assert not chap4.more_vowels('good')
    assert not chap4.more_vowels('count')
    assert chap4.more_vowels('you')
    assert chap4.more_vowels('foo')
    assert chap4.more_vowels('trainee')
    assert chap4.more_vowels('eye')


def test_evens_first():
    """Solution to exercise C-4.19.

    Write a short recursive Python function that rearranges a sequence of
    integer values so that all the even values appear before all the odd
    values.
    """
    np.random.seed = 19
    test1 = list(range(10))
    result1 = chap4.evens_first(test1)
    for idx in range(5):
        assert result1[idx] % 2 == 0
    test2 = list(np.random.randint(0, 1000, size=100))
    result2 = chap4.evens_first(test2)
    odds_start = None
    for idx, num in enumerate(result2):
        if num % 2 == 1:
            if odds_start is None:
                odds_start = idx
        else:
            if odds_start is not None:
                assert False


def test_rearrange_unsorted():
    """Solution to exercise C-4.20.

    Given an unsorted sequence, S, of integers and an integer k, describe a
    recursive algorithm for rearranging the elements in S so that all elements
    less than or equal to k come before any elements larger than k. What is
    the running time of your algorithm on a sequence of n values?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The algorithm terminates when the start index equals the stop index.  That
    requires n recursive calls.  Each recursive call will worst case swap two
    values in the list.  Replacing a value in a list is O(1) according to the
    text (table 5.4), and so this algorithm is O(n).
    """
    test1 = [99, 88, 77, 103, 22, 4, 19, 62, 53]
    k1 = 65
    result1 = chap4.rearrange_unsorted(test1, k1)
    for idx, num in enumerate(result1):
        if idx < 5:
            assert num <= k1
        else:
            assert num > k1


def test_sum_to_k():
    """Solution to exercise C-4.21.

    Suppose you are given an n-element sequence, S, containing distinct
    integers that are listed in increasing order. Given a number k, describe a
    recursive algorithm to find two integers in S that sum to k, if such a pair
    exists. What is the running time of your algorithm?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    """
    test1 = list(range(10))
    k_list = [0, 1, 2, 11, 14, 17, 18, 19, 20]
    for k in k_list:
        if k in [0, 18, 19, 20]:
            assert chap4.sum_to_k(test1, k) is None
        else:
            assert sum(chap4.sum_to_k(test1, k)) == k


# %% Project Exercises
@pytest.mark.parametrize('word1, word2, word3',
                         [['pot', 'pan', 'bib'],
                          ['dog', 'cat', 'pig'],
                          ['boy', 'girl', 'baby']
                          ])
def test_summation_puzzle(word1, word2, word3):
    """Solution to exercise P-4.24.

    Write a program for solving summation puzzles by enumerating and testing
    all possible configurations. Using your program, solve the three puzzles
    given in Section 4.4.3.
    """
    _, char_dict = chap4.summation_puzzle([word1, word2, word3])
    str1 = [str(char_dict[x]) for x in word1]
    val1 = int(''.join(str1))
    str2 = [str(char_dict[x]) for x in word2]
    val2 = int(''.join(str2))
    str3 = [str(char_dict[x]) for x in word3]
    val3 = int(''.join(str3))
    assert (val1 + val2) == val3


def test_os_walk(tmp_path):
    """Solution to exercise P-4.27.

    Python’s os module provides a function with signature walk(path) that
    is a generator yielding the tuple (dirpath, dirnames, filenames) for each
    subdirectory of the directory identified by string path, such that string
    dirpath is the full path to the subdirectory, dirnames is a list of the
    names of the subdirectories within dirpath, and filenames is a list of the
    names of non-directory entries of dirpath.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I used pytest's tmp_path fixture to create a temporary directory with a
    function-level scope.  I then wrote a recursive function to create a simple
    directory with multiple levels of subdirectories and files.

    I compare the results of the os module's walk function to my own.  Note
    that the order of the tuples reported by the two methods may be arbitrary,
    and so I sorted both results before comparing them.  I also compared the
    lists of files and directories as sets so that a differing order does not
    cause the test to fail.
    """
    files = ['testa.txt', 'testb.txt', 'testc.txt']
    dirs = ['dir1', 'dir2', 'dir3']
    max_depth = 4

    def create_subdir(path, level):
        if level == max_depth:
            return  # Base case, deepest level of directory reached
        for subdir in dirs:
            temp_dir = path / (f'l{level}_' + subdir)
            temp_dir.mkdir()
            for file in files:
                temp_file = temp_dir / (f'l{level+1}_' + file)
                temp_file.write_text(f'l{level+1}_' + file)
            create_subdir(path / temp_dir, level+1)

    create_subdir(tmp_path, 1)
    results = chap4.os_walk(tmp_path)
    results.sort()
    expected_results = list(os.walk(tmp_path))
    expected_results.sort()
    for expected, result in zip(expected_results, results):
        assert expected[0] == result[0]
        assert set(expected[1]) == set(result[1])
        assert set(expected[2]) == set(result[2])
