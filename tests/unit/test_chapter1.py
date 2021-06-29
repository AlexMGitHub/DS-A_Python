#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 1 exercises.

###############################################################################
# test_chapter1.py
#
# Revision:     1.00
# Date:         6/22/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 1 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports
import random
from array import array
from unittest.mock import patch

# Related third party imports
import numpy as np
import pytest

# Local application/library specific imports
import dsa.chapter1_exercises as chap1


# %% Reinforcement Exercises
def test_is_multiple():
    """Solution to exercise R-1.1.

    Returns True if n is a multiple of m, that is, n = mi for some integer i,
    and False otherwise.
    """
    assert chap1.is_multiple(20, 4)
    assert chap1.is_multiple(33, 11)
    assert not chap1.is_multiple(26, 3)
    assert not chap1.is_multiple(20, 6)


def test_is_even():
    """Solution to exercise R-1.2.

    Takes an integer value and returns True if k is even, and False otherwise.
    However, the function cannot use the multiplication, modulo, or division
    operators.
    """
    assert chap1.is_even(2)
    assert chap1.is_even(26)
    assert chap1.is_even(138)
    assert not chap1.is_even(3)
    assert not chap1.is_even(35)
    assert not chap1.is_even(111)


def test_minmax():
    """Solution to exercise R-1.3.

    Takes a sequence of one or more numbers, and returns the smallest and
    largest numbers, in the form of a tuple of length two. Do not use the
    built-in functions min or max in implementing the solution.
    """
    np.random.seed = 111
    data1 = list(np.random.randint(0, 1000, size=100))
    data2 = tuple(np.random.randint(0, 1000, size=50))
    data3 = list(np.random.randint(0, 1000, size=1000))
    assert chap1.minmax(data1) == (min(data1), max(data1))
    assert chap1.minmax(data2) == (min(data2), max(data2))
    assert chap1.minmax(data3) == (min(data3), max(data3))


def test_sum_of_squares():
    """Solution to exercise R-1.4.

    Takes a positive integer n and returns the sum of the squares of all the
    positive integers smaller than n.
    """
    assert chap1.sum_of_squares(5) == 30
    assert chap1.sum_of_squares(3) == 5
    assert chap1.sum_of_squares(6) == 55
    assert chap1.sum_of_squares(10) == 285


def test_sos_one_line():
    """Solution to exercise R-1.5.

    Give a single command that computes the sum from Exercise R-1.4, relying
    on Python’s comprehension syntax and the built-in sum function.
    """
    assert chap1.sos_one_line(5) == 30
    assert chap1.sos_one_line(3) == 5
    assert chap1.sos_one_line(6) == 55
    assert chap1.sos_one_line(10) == 285


def test_sos_odd():
    """Solution to exercise R-1.6.

    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.
    """
    assert chap1.sos_odd(5) == 10
    assert chap1.sos_odd(3) == 1
    assert chap1.sos_odd(6) == 35
    assert chap1.sos_odd(10) == 165


def test_sos_odd_one_line():
    """Solution to exercise R-1.7.

    Give a single command that computes the sum from Exercise R-1.6, relying
    on Python’s comprehension syntax and the built-in sum function.
    """
    assert chap1.sos_odd_one_line(5) == 10
    assert chap1.sos_odd_one_line(3) == 1
    assert chap1.sos_odd_one_line(6) == 35
    assert chap1.sos_odd_one_line(10) == 165


def test_string_index():
    """Solution to exercise R-1.8.

    Python allows negative integers to be used as indices into a sequence,
    such as a string. If string s has length n, and expression s[k] is used for
    index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j]
    references the same element?
    """
    string1 = 'abcdef'
    string2 = 'Hello, world!'
    string3 = 'Testing 1, 2, 3...'
    strings = [string1, string2, string3]
    for string in strings:
        for idx in range(len(string), 0, -1):
            assert string[chap1.string_index(-idx, string)] == string[-idx]


def test_range_constructor9():
    """Solution to exercise R-1.9.

    What parameters should be sent to the range constructor, to produce a
    range with values 50, 60, 70, 80?
    """
    assert list(chap1.range_constructor9()) == [50, 60, 70, 80]


def test_range_constructor10():
    """Solution to exercise R-1.10.

    What parameters should be sent to the range constructor, to produce a
    range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
    """
    assert list(chap1.range_constructor10()) == [8, 6, 4, 2, 0, -2, -4, -6, -8]


def test_list_comprehension():
    """Solution to exercise R-1.11.

    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
    """
    assert chap1.list_comprehension() == [1, 2, 4, 8, 16, 32, 64, 128, 256]


def test_random_randrange():
    """Solution to exercise R-1.12.

    Python’s random module includes a function choice(data) that returns a
    random element from a non-empty sequence. The random module in-
    cludes a more basic function randrange, with parameterization similar to
    the built-in range function, that return a random choice from the given
    range. Using only the randrange function, implement your own version
    of the choice function.
    """
    random.seed(11)
    test_list = list(range(20, 40))
    a = random.choice(test_list)
    b = random.choice(test_list)
    c = random.choice(test_list)
    random.seed(11)
    a2 = chap1.random_randrange(test_list)
    b2 = chap1.random_randrange(test_list)
    c2 = chap1.random_randrange(test_list)
    assert (a, b, c) == (a2, b2, c2)


# %% Creativity Exercises
def test_reverse_list():
    """Solution to exercise C-1.13.

    Write a pseudo-code description of a function that reverses a list of n
    integers, so that the numbers are listed in the opposite order than they
    were before, and compare this method to an equivalent Python function
    for doing the same thing.
    """
    integer_list = list(range(0, 10))
    test_reverse = chap1.reverse_list(integer_list)
    integer_list.reverse()
    assert test_reverse == integer_list


def test_odd_pair():
    """Solution to exercise C-1.14.

    Write a short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose
    product is odd.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The product of two odd numbers will produce an odd number.  If there are at
    least two (unique) odd numbers in the sequence, the function should return
    True.
    """
    alist = [1, 2, 3, 4, 5]
    blist = [3, 3, 3, 4, 6, 8, 10]
    clist = [10, 20, 30, 40, 50]
    dlist = [9, 7, 7, 4, 16, 22]
    assert chap1.odd_pair(alist)
    assert not chap1.odd_pair(blist)
    assert not chap1.odd_pair(clist)
    assert chap1.odd_pair(dlist)


def test_check_unique():
    """Solution to exercise C-1.15.

    Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other (that is, they are
    distinct).
    """
    alist = [1, 2, 3, 4, 5]
    blist = [3, 3, 3, 4, 6, 8, 10]
    clist = [10, 20, 30, 40, 50]
    dlist = [9, 7, 7, 4, 16, 22]
    assert chap1.check_unique(alist)
    assert not chap1.check_unique(blist)
    assert chap1.check_unique(clist)
    assert not chap1.check_unique(dlist)


def test_scale16():
    """Solution to exercise C-1.16.

    In our implementation of the scale function (page 25), the body of the loop
    executes the command data[j] *= factor. We have discussed that numeric
    types are immutable, and that use of the *= operator in this context causes
    the creation of a new instance (not the mutation of an existing instance).
    How is it still possible, then, that our implementation of scale changes
    the actual parameter sent by the caller?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    In the implementation of the scale function on page 25, "data" is an alias
    (formal parameter) of the actual parameter that refers to a mutable list
    object.

    From the text, page 16:
    "For an immutable type, such as a number or a string, one should not
    presume that this syntax changes the value of the existing object, but
    instead that it will reassign the identifier to a newly constructed value.
    However, it is possible for a type to redefine such semantics to mutate the
    object, as the list class does for the += operator."

    And from page 15 of the text:
    "Because lists are mutable, the syntax s[j] = val can be used to replace an
    element at a given index."
    """
    assert chap1.scale16()


def test_scale17():
    """Solution to exercise C-1.17.

    Had we implemented the scale function (page 25) as follows, does it work
    properly?

    def scale(data, factor):
        for val in data:
            val *= factor

    Explain why or why not.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    No, it doesn't work.  Per the text, page 21:

    "It is worth noting that val is treated as a standard identifier. If the
    element of the original data happens to be mutable, the val identifier can
    be used to invoke its methods. But a reassignment of identifier val to a
    new value has no affect on the original data, nor on the next iteration of
    the loop."

    The code above fails because it tries to assign a new value to the "val"
    identifier.  This merely breaks the alias without changing the list.
    """
    nums = list(range(10))
    factor = 4
    scaled_nums = [num * factor for num in nums]
    assert chap1.scale17(nums, factor) == nums
    assert chap1.scale17(nums, factor) != scaled_nums


def test_list_comp18():
    """Solution to exercise C-1.18.

    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
    """
    assert chap1.list_comp18() == [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]


def test_abc19():
    """Solution to exercise C-1.19.

    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [ a , b , c , ..., z ], but without having to type all 26 such
    characters literally.
    """
    expected = list('abcdefghijklmnopqrstuvwxyz')
    assert chap1.abc19() == expected


def test_rand_shuffle():
    """Solution to exercise C-1.20.

    Python’s random module includes a function shuffle(data) that accepts a
    list of elements and randomly reorders the elements so that each possi-
    ble order occurs with equal probability. The random module includes a
    more basic function randint(a, b) that returns a uniformly random integer
    from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function.
    """
    random.seed(38)
    test_list = list(range(20, 40))
    test_list2 = test_list.copy()
    random.shuffle(test_list2)
    random.seed(38)
    chap1.rand_shuffle(test_list)
    assert test_list == test_list2


def test_user_input():
    """Solution to exercise C-1.21.

    Write a Python program that repeatedly reads lines from standard input
    until an EOFError is raised, and then outputs those lines in reverse order
    (a user can indicate end of input by typing ctrl-D).
    """
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['Hello, World!', 'Nice to', 'meet', 'you!',
                                  EOFError]
        reversed_output = chap1.user_input()
        assert reversed_output == ['you!', 'meet', 'Nice to', 'Hello, World!']


def test_dot_product():
    """Solution to exercise C-1.22.

    Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it
    returns an array c of length n such that c[i] = a[i] · b[i], for i = 0, .
    . . , n − 1.
    """
    random.seed(45)
    a = array('i', random.sample(range(100), 10))
    b = array('i', random.sample(range(100), 10))
    c = array('i', range(0, 10))
    assert (chap1.dot_product(a, b) == np.multiply(a, b)).all()
    assert chap1.dot_product(c, c) == array('i', [0, 1, 4, 9, 16, 25, 36, 49,
                                                  64, 81])


def test_out_of_bounds():
    """Solution to exercise C-1.23.

    Give an example of a Python code fragment that attempts to write an ele-
    ment to a list based on an index that may be out of bounds. If that index
    is out of bounds, the program should catch the exception that results, and
    print the following error message:
    “Don’t try buffer overflow attacks in Python!”
    """
    test_list = [1, 5, 8, 13, 4]
    assert chap1.out_of_bounds(test_list, 3, 27) == [1, 5, 8, 27, 4]
    assert chap1.out_of_bounds(test_list, 4, 18) == [1, 5, 8, 27, 18]
    assert chap1.out_of_bounds(test_list, 5, 54) == [1, 5, 8, 27, 18]
    assert chap1.out_of_bounds(test_list, 0, 99) == [99, 5, 8, 27, 18]


def test_count_vowels():
    """Solution to exercise C-1.24.

    Write a short Python function that counts the number of vowels in a given
    character string.
    """
    string = 'Hello, World!  Nice to meet you!'
    assert chap1.count_vowels(string) == 10


def test_remove_punctuation():
    """Solution to exercise C-1.25.

    Write a short Python function that takes a string s, representing a
    sentence, and returns a copy of the string with all punctuation removed.
    For example, if given the string "Let s try, Mike.", this function would
    return "Lets try Mike".
    """
    string = "Let's try, Mike."
    assert chap1.remove_punctuation(string) == "Lets try Mike"


def test_correct_arithmetic():
    """Solution to exercise C-1.26.

    Write a short program that takes as input three integers, a, b, and c, from
    the console and determines if they can be used in a correct arithmetic
    formula (in the given order), like “a + b = c,” “a = b − c,”
    or “a ∗ b = c.”

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Arithmetic operators are listed on page 13 and include: +, - *, /, //, %.
    There are only two possible positions to place an arithmetic operator, and
    one of the positions must be an assignment (=).  There should then be 12
    possibilities to check for the 6 operators.
    """
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['1', '2', '3']  # Addition, left position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['1', '0', '1']  # Addition, right position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['2', '3', '-1']  # Subtraction, left position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['2', '3', '1']  # Subtraction, right position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['2', '2', '4']  # Multiplication, left pos
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['10', '5', '2']  # Multiplication, right pos
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['4', '2', '2']  # Division, left position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['5', '10', '2']  # Division, right position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['5', '2', '2']  # Integer div, left position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['3', '10', '3']  # Integer div, right pos
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['5', '2', '1']  # Modulus, left position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['3', '8', '5']  # Modulus, right position
        assert chap1.correct_arithmetic()
        mock_input.side_effect = ['4', '5', '6']  # No valid operations
        assert not chap1.correct_arithmetic()
        mock_input.side_effect = ['-2', '2', '5']  # No valid operations
        assert not chap1.correct_arithmetic()
        mock_input.side_effect = ['17', '3', '10']  # No valid operations
        assert not chap1.correct_arithmetic()
        mock_input.side_effect = ['-2', '0', '11']  # No valid operations
        assert not chap1.correct_arithmetic()


def test_compute_factor():
    """Solution to exercise C-1.27.

    In Section 1.8, we provided three different implementations of a generator
    that computes factors of a given integer. The third of those
    implementations, from page 41, was the most efficient, but we noted that
    it did not yield the factors in increasing order. Modify the generator so
    that it reports factors in increasing order, while maintaining its general
    performance advantages.
    """
    n = 100
    assert list(chap1.compute_factor(n)) == [1, 2, 4, 5, 10, 20, 25, 50, 100]


def test_p_norm():
    """Solution to exercise C-1.28.

    Give an implementation of a function named norm such that norm(v, p)
    returns the p-norm value of v and norm(v) returns the Euclidean norm of v.
    You may assume that v is a list of numbers.
    """
    test_list = list(range(5))
    assert chap1.p_norm(test_list) == 30 ** 0.5
    assert chap1.p_norm(test_list, 2) == 30 ** 0.5
    assert chap1.p_norm(test_list, 3) == 100 ** (1/3)
    assert chap1.p_norm(test_list, 4) == 354 ** (1/4)


# %% Project Exercises
def test_catdog():
    """Solution to exercise P-1.29.

    Write a Python program that outputs all possible strings formed by using
    the characters c , a , t , d , o , and g exactly once.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A permutation of n elements without repetition has n! possible
    permutations.  'Catdog' should have 6! = 720 unique permutations.  Use
    recursion to swap characters and produce every possible permutation.
    """
    permutations = chap1.catdog(list('ABC'))
    assert len(permutations) == 6
    assert len(permutations) == len(set(permutations))
    assert set(permutations) == set(['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB'])
    permutations = chap1.catdog(list('catdog'))
    assert len(permutations) == 720
    assert len(permutations) == len(set(permutations))


def test_two_divider():
    """Solution to exercise P-1.30.

    Write a Python program that can take a positive integer greater than 2
    as input and write out the number of times one must repeatedly divide
    this number by 2 before getting a value less than 2.
    """
    invalid_nums = [1, 0, -1, -10, 2, 10.4]
    for num in invalid_nums:
        with pytest.raises(ValueError):
            chap1.two_divider(num)
    assert chap1.two_divider(30) == 4
    assert chap1.two_divider(35) == 5
    assert chap1.two_divider(4) == 2
    assert chap1.two_divider(6) == 2
    assert chap1.two_divider(8) == 3
    assert chap1.two_divider(100) == 6
    assert chap1.two_divider(1000) == 9


def test_make_change():
    """Solution to exercise P-1.31.

    Write a Python program that can “make change.” Your program should
    take two numbers as input, one that is a monetary amount charged and the
    other that is a monetary amount given. It should then return the number
    of each kind of bill and coin to give back as change for the difference
    between the amount given and the amount charged. The values assigned
    to the bills and coins can be based on the monetary system of any current
    or former government. Try to design your program so that it returns as
    few bills and coins as possible.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The largest bill I will use is a 100 dollar bill, and I will not use
    uncommon denominations such as two dollar bills or half dollar coins.
    Convert all values to decimal data type to avoid annoying arithmetic
    errors.
    """
    with pytest.raises(AssertionError):
        chap1.make_change(4.22, 3.80)
    result1 = chap1.make_change(6.79, 10)
    expected1 = {'1_dollar': 3, 'dime': 2, 'penny': 1, 'Total change': '$3.21'}
    result2 = chap1.make_change(19.99, 100)
    expected2 = {
        '50_dollar':      1,
        '20_dollar':      1,
        '10_dollar':      1,
        'penny':          1,
        'Total change':   '$80.01'
    }
    assert result1 == expected1
    assert result2 == expected2


def test_simple_calculator(capsys):
    """Solution to exercise P-1.32.

    Write a Python program that can simulate a simple calculator, using the
    console as the exclusive input and output device. That is, each input to
    the calculator, be it a number, like 12.34 or 1034, or an operator, like +
    or =, can be done on a separate line. After each such input, you should
    output to the Python console what would be displayed on your calculator.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    This exercise is very similar to P-1.33.  I have restricted the simple
    calculator to clear its memory whenever the '=' key is pressed.  The next
    exercise will allow the user to manually clear memory.
    """
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['4', '*', '21', '=', 'q']
        chap1.simple_calculator()
        captured = capsys.readouterr()
        assert "= 84\n" in captured.out
        mock_input.side_effect = ['59', '-', '65', '=', 'q']
        chap1.simple_calculator()
        captured = capsys.readouterr()
        assert "= -6\n" in captured.out
        mock_input.side_effect = ['10', '/', '3', '=', 'q']
        chap1.simple_calculator()
        captured = capsys.readouterr()
        assert "= 3.3333\n" in captured.out
        mock_input.side_effect = ['1', '/', '8', '=', 'q']
        chap1.simple_calculator()
        captured = capsys.readouterr()
        assert "= 0.125\n" in captured.out
        mock_input.side_effect = ['5', '+', '4', '+', '3', '+', '2', '+', '1',
                                  '=', 'q']
        chap1.simple_calculator()
        captured = capsys.readouterr()
        assert "= 15\n" in captured.out
        mock_input.side_effect = ['5', '*', '+', 'q']
        chap1.simple_calculator()
        captured = capsys.readouterr()
        assert "Invalid input!" in captured.out


def test_handheld_calculator(capsys):
    """Solution to exercise P-1.33.

    Write a Python program that simulates a handheld calculator. Your pro-
    gram should process input from the Python console representing buttons
    that are “pushed,” and then output the contents of the screen after each
    operation is performed. Minimally, your calculator should be able to
    process the basic arithmetic operations and a reset/clear operation.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I'm not clear on what the authors are getting at here.  This calculator
    operates the same as in P-1.32 except that it has a manual clear function.
    The previous calculation will be kept in memory unless manually cleared
    by the user.
    """
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['36', '*', '10', '=', 'q']
        chap1.handheld_calculator()
        captured = capsys.readouterr()
        assert "= 360\n" in captured.out
        mock_input.side_effect = ['36', '*', '10', '=', '/', '12', '/', '5',
                                  '=', '/', '3', '=', 'q']
        chap1.handheld_calculator()
        captured = capsys.readouterr()
        assert "= 2\n" in captured.out
        mock_input.side_effect = ['5', '+', '17', '=', 'cls', '45', '-',
                                  '18.5', '=', 'q']
        chap1.handheld_calculator()
        captured = capsys.readouterr()
        assert "= 26.5\n" in captured.out
        mock_input.side_effect = ['10', '/', '3', '=', 'q']
        chap1.handheld_calculator()
        captured = capsys.readouterr()
        assert "= 3.3333\n" in captured.out
        mock_input.side_effect = ['5', '*', '+', 'q']
        chap1.handheld_calculator()
        captured = capsys.readouterr()
        assert "Invalid input!" in captured.out
        mock_input.side_effect = ['+', 'q']
        chap1.handheld_calculator()
        captured = capsys.readouterr()
        assert "Invalid input!" in captured.out


def test_punishment():
    """Solution to exercise P-1.34.

    A common punishment for school children is to write out a sentence mul-
    tiple times. Write a Python stand-alone program that will write out the
    following sentence one hundred times: “I will never spam my friends
    again.” Your program should number each of the sentences and it should
    make eight different random-looking typos.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I will createa  list with 100 copies of the sentence, then sample the list
    without replacement to choose 8 sentences to create typos.  For each of the
    8 sentences, I will sample 2 characters without replacement to swap
    positions, then I'll check to make sure that the typo is unique.
    """
    random.seed(95)
    result = chap1.punishment()
    numberless = [x[-35:] for x in result]
    assert len(result) == 100
    assert len(set(numberless)) == 9  # Original sentence plus 8 with typos


def test_birthday_paradox():
    """Solution to exercise P-1.35..

    The birthday paradox says that the probability that two people in a room
    will have the same birthday is more than half, provided n, the number of
    people in the room, is more than 23. This property is not really a paradox,
    but many people find it surprising. Design a Python program that can test
    this paradox by a series of experiments on randomly generated birthdays,
    which test this paradox for n = 5, 10, 15, 20, . . . , 100.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I will represent the days of the year with integers ranging from 1 to 365.
    However, a leap year adds another day every four years.  To properly
    represent the odds of being born on a leap day, I will include 4 copies
    of the values between 1 and 365, and only one copy of the value 366.  This
    works out to a chance of 1 in 1461 to be born on a leap day.
    """
    random.seed(66)
    assert chap1.birthday_paradox(5) < 0.5
    assert chap1.birthday_paradox(10) < 0.5
    assert chap1.birthday_paradox(15) < 0.5
    assert chap1.birthday_paradox(20) < 0.5
    assert chap1.birthday_paradox(30) > 0.5
    assert chap1.birthday_paradox(50) > 0.5
    assert chap1.birthday_paradox(100) > 0.5


def test_count_words():
    """Solution to exercise P-1.36..

    Write a Python program that inputs a list of words, separated by white-
    space, and outputs how many times each word appears in the list. You
    need not worry about efficiency at this point, however, as this topic is
    something that will be addressed later in this book.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I will split the sentence into a list using the whitespace as a delimiter.
    The resulting words will be cleaned of punctuation using the previously
    written remove_punctuation() function.  The lowercase version of each word
    will be checked as a key against a dictionary of words, and if the key
    exists its value will be incremented by one.  The function will return the
    resulting dictionary that contains the words of the sentence as keys, and
    the number of times the words appear as values.
    """
    sentence = "Peter Piper picked a peck of pickled peppers A peck of "\
        "pickled peppers Peter Piper picked If Peter Piper picked a peck of "\
        "pickled peppers Where's the peck of pickled peppers Peter Piper "\
        "picked?"
    result = chap1.count_words(sentence)
    assert result['peter'] == 4
    assert result['pickled'] == 4
    assert result['peppers'] == 4
    assert result['peck'] == 4
    assert result['picked'] == 4
