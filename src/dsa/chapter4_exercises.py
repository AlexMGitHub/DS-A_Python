#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 4 exercises.

###############################################################################
# chapter4_exercises.py
#
# Revision:     1.00
# Date:         6/27/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 4 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports
from pathlib import Path


# %% Reinforcement Exercises
def harmonic_number(n):
    """Solution to exercise R-4.6.

    Describe a recursive function for computing the nth Harmonic number.
    """
    if n == 1:
        return 1/n  # Base case
    return 1/n + harmonic_number(n-1)


def str_to_int(string):
    """Solution to exercise R-4.7.

    Describe a recursive function for converting a string of digits into the
    integer it represents. For example, "13531" represents the integer 13,531.
    """
    n = len(string)
    zero_unicode = ord('0')

    def recurse(idx):
        if idx == n:
            return 0  # Base case
        int_val = ord(string[idx]) - zero_unicode
        return int_val * 10 ** (n - 1 - idx) + recurse(idx + 1)

    return recurse(0)


# %% Creativity Exercises
def find_min_max(data):
    """Solution to exercise C-4.9.

    Write a short recursive Python function that finds the minimum and
    maximum values in a sequence without using any loops.
    """
    n = len(data)
    min_val = data[0]
    max_val = data[0]

    def recurse_minmax(idx):
        nonlocal min_val, max_val
        if idx == n:
            return min_val, max_val  # Base case
        if data[idx] > max_val:
            max_val = data[idx]
        elif data[idx] < min_val:
            min_val = data[idx]
        return recurse_minmax(idx + 1)

    return recurse_minmax(1)


def recursive_log(num):
    """Solution to exercise C-4.10.

    Describe a recursive algorithm to compute the integer part of the base-two
    logarithm of n using only addition and integer division.
    """

    def recurse(num, count):
        if num == 1:
            return count  # Base case
        return recurse(num // 2, count + 1)

    return recurse(num, 0)


def recursive_unique(sequence):
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
    recursion algorithm.

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
    n = len(sequence)

    def unique(start, stop):
        if sequence[start] == sequence[stop]:
            return False  # Base case if not unique
        if stop > (start+1):
            return unique(start, stop-1)
        if start < (n-2):
            return unique(start+1, n-1)
        return True  # Base case if unique

    return unique(0, n-1)


def integer_product(num1, num2):
    """Solution to exercise C-4.12.

    Give a recursive algorithm to compute the product of two positive integers,
    m and n, using only addition and subtraction.
    """

    def recurse(num1, idx):
        if idx == 0:
            return 0  # Base case
        return num1 + recurse(num1, idx-1)

    return recurse(num1, num2)


def towers_of_hanoi(n):
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
    a = list(range(n, 0, -1))
    b = []
    c = []

    def recurse(n, source, destination, temp):
        if n > 0:  # Base case, bottom of stack of disks
            # Move n-1 disks from source to temporary storage
            recurse(n-1, source, temp, destination)
            # Move the nth (bottom) disk from source to destination
            destination.append(source.pop())
            # Move the n-1 disks from temporary storage to destination
            recurse(n-1, temp, destination, source)
    recurse(n, a, c, b)
    return c


def all_subsets(aset):
    """Solution to exercise C-4.15.

    Write a recursive function that will output all the subsets of a set of n
    elements (without repeating any subsets).

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I've made the following assumptions:
        1. The input is a list of unique numbers
        2. The set itself is considered a subset (not a proper subset)
        3. The empty set is considered a subset
    """

    def recurse(alist):
        if not alist:
            return [[]]  # Base case, return empty set
        prev_lists = recurse(alist[1:])
        return prev_lists + [[alist[0]] + y for y in prev_lists]

    return recurse(aset)


def reverse_string(string):
    """Solution to exercise C-4.16.

    Write a short recursive Python function that takes a character string s and
    outputs its reverse. For example, the reverse of "pots&pans" would be
    "snap&stop".
    """
    n = len(string)

    def recurse(idx):
        if idx == 0:
            return string[0]  # Base case, decremented to beginning of string
        return string[idx] + recurse(idx-1)

    return recurse(n-1)


def is_palindrome(string):
    """Solution to exercise C-4.17.

    Write a short recursive Python function that determines if a string s is a
    palindrome, that is, it is equal to its reverse. For example, "racecar"
    and "gohangasalamiimalasagnahog" are palindromes.
    """
    n = len(string)

    def recurse(idx):
        if idx == n:
            return True  # Base case, end of string and all letters matched
        if string[idx] == string[n-1-idx]:
            return recurse(idx+1)
        return False

    return recurse(0)


def more_vowels(astring):
    """Solution to exercise C-4.18.

    Use recursion to write a Python function for determining if a string s has
    more vowels than consonants.
    """
    string = astring.lower()
    vowels = 'aeiou'
    n = len(string)
    vowel_count = 0

    def recurse(idx):
        nonlocal vowel_count
        if idx == n:
            return vowel_count > (n-vowel_count)  # Base case, end of string
        if string[idx] in vowels:
            vowel_count += 1
        return recurse(idx+1)

    return recurse(0)


def evens_first(nums):
    """Solution to exercise C-4.19.

    Write a short recursive Python function that rearranges a sequence of
    integer values so that all the even values appear before all the odd
    values.
    """
    n = len(nums)

    def recurse(start, stop):
        if start == stop:
            return nums  # Base case, finished sorting list
        if nums[start] % 2 == 0:
            return recurse(start+1, stop)
        nums[stop], nums[start] = nums[start], nums[stop]
        return recurse(start, stop-1)

    return recurse(0, n-1)


def rearrange_unsorted(nums, k):
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
    n = len(nums)

    def recurse(start, stop):
        if start == stop:
            return nums  # Base case, finished sorting list
        if nums[start] <= k:
            return recurse(start+1, stop)
        nums[stop], nums[start] = nums[start], nums[stop]
        return recurse(start, stop-1)

    return recurse(0, n-1)


def sum_to_k(nums, k):
    """Solution to exercise C-4.21.

    Suppose you are given an n-element sequence, S, containing distinct
    integers that are listed in increasing order. Given a number k, describe a
    recursive algorithm to find two integers in S that sum to k, if such a pair
    exists. What is the running time of your algorithm?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    All of the non-recursive operations are O(1).  The running time is thus
    proportional to the number of recursive calls.  Worst case, the algorithm
    will try every pairwise combination in the sequence.  This is O(n^2), as
    there are n elements, each of which will be compared with n - k other
    elements: the familiar n*(n+1)/2 formula.
    """
    n = len(nums)

    def recurse(start, stop):
        if nums[start] + nums[stop] == k:
            return nums[start], nums[stop]  # Base case: pair found
        if stop > (start+1):
            return recurse(start, stop-1)
        if start < (n-2):
            return recurse(start+1, n-1)
        return None                         # Base case: no pair found

    return recurse(0, n-1)


# %% Project Exercises
def summation_puzzle(words):
    """Solution to exercise P-4.24.

    Write a program for solving summation puzzles by enumerating and testing
    all possible configurations. Using your program, solve the three puzzles
    given in Section 4.4.3.
    """
    assert len(words) == 3, 'Summation puzzle must be three word phrase'
    digit_list = list(range(10))
    chars = list(''.join(words))
    unique_chars = list(set(chars))
    n = len(unique_chars)
    char_dict = {}

    def solution_found(S):
        nonlocal char_dict
        char_dict = {unique_chars[idx]: S[idx] for idx in range(len(S))}
        word1 = [str(char_dict[x]) for x in words[0]]
        val1 = int(''.join(word1))
        word2 = [str(char_dict[x]) for x in words[1]]
        val2 = int(''.join(word2))
        word3 = [str(char_dict[x]) for x in words[2]]
        val3 = int(''.join(word3))
        return (val1 + val2) == val3

    def recurse(k, S, U):
        for idx, e in enumerate(U):
            S.append(U.pop(idx))
            if k == 1:
                if solution_found(S):
                    return (S, char_dict)  # Base case: Solution found
            else:
                result = recurse(k-1, S.copy(), U.copy())
                if result is not None:
                    return result
            S.pop()
            U.insert(0, e)
        return None  # Base case: No solution found

    return recurse(n, [], digit_list)


def os_walk(path_str, topdown=False):
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
    results = []
    path = Path(path_str)

    def walk(path):
        files = []
        dirs = []
        contents = Path.iterdir(path)
        for obj in contents:
            if Path.is_dir(obj):
                dirs.append(obj.name)
                walk(obj)
            else:
                files.append(obj.name)
        results.append((str(path), dirs, files))

    walk(path)
    if topdown:
        results.reverse()  # os.walk defaults to topdown = True
    return results
