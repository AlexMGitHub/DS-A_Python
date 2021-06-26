#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###############################################################################
# chapter1_exercises.py
#
# Revision:     1.00
# Date:         6/22/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 1 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports
import random
import math
from decimal import Decimal
from array import array


# %% Reinforcement Exercises
def is_multiple(n, m):
    """R-1.1
    Returns True if n is a multiple of m, that is, n = mi for some
    integer i, and False otherwise.
    """
    return n % m == 0


def is_even(k):
    """R-1.2
    Takes an integer value and returns True if k is even, and False
    otherwise. However, the function cannot use the multiplication, modulo, or
    division operators.
    """
    k_str = str(k)
    last_digit = int(k_str[-1])
    return last_digit in [0, 2, 4, 6, 8]


def minmax(data):
    """R-1.3
    Takes a sequence of one or more numbers, and returns the smallest and
    largest numbers, in the form of a tuple of length two. Do not use the
    built-in functions min or max in implementing the solution.
    """
    min_idx = 0
    max_idx = 0
    for idx, num in enumerate(data):
        if num > data[max_idx]:
            max_idx = idx
        if num < data[min_idx]:
            min_idx = idx
    return (data[min_idx], data[max_idx])


def sum_of_squares(n):
    """R-1.4
    Takes a positive integer n and returns the sum of the squares of all the
    positive integers smaller than n.
    """
    squares = 0
    for num in range(1, n):
        squares += num ** 2
    return squares


def sos_one_line(n):
    """R-1.5
    Give a single command that computes the sum from Exercise R-1.4, relying
    on Python’s comprehension syntax and the built-in sum function.
    """
    return sum([num ** 2 for num in range(1, n)])


def sos_odd(n):
    """R-1.6
    Write a short Python function that takes a positive integer n and returns
    the sum of the squares of all the odd positive integers smaller than n.
    """
    squares = 0
    for num in range(1, n, 2):
        squares += num ** 2
    return squares


def sos_odd_one_line(n):
    """R-1.7
    Give a single command that computes the sum from Exercise R-1.6, relying
    on Python’s comprehension syntax and the built-in sum function.
    """
    return sum([num ** 2 for num in range(1, n, 2)])


def string_index(neg_idx, string):
    """R-1.8
    Python allows negative integers to be used as indices into a sequence,
    such as a string. If string s has length n, and expression s[k] is used for
    index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j]
    references the same element?
    """
    n = len(string)
    return n + neg_idx


def range_constructor9():
    """R-1.9
    What parameters should be sent to the range constructor, to produce a
    range with values 50, 60, 70, 80?
    """
    return range(50, 90, 10)


def range_constructor10():
    """R-1.10
    What parameters should be sent to the range constructor, to produce a
    range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
    """
    return range(8, -10, -2)


def list_comprehension():
    """R-1.11
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
    """
    return [2 ** x for x in range(0, 9)]


def random_randrange(test_list):
    """R-1.12
    Python’s random module includes a function choice(data) that returns a
    random element from a non-empty sequence. The random module in-
    cludes a more basic function randrange, with parameterization similar to
    the built-in range function, that return a random choice from the given
    range. Using only the randrange function, implement your own version
    of the choice function.
    """
    idx = random.randrange(0, len(test_list))
    return test_list[idx]


# %% Creativity Exercises
def reverse_list(integer_list):
    """C-1.13
    Write a pseudo-code description of a function that reverses a list of n
    integers, so that the numbers are listed in the opposite order than they
    were before, and compare this method to an equivalent Python function
    for doing the same thing.
    """
    return integer_list[::-1]


def odd_pair(nums):
    """C-1.14
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
    uniques = set(nums)
    odd_count = 0
    for num in uniques:
        if num % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                break
    return odd_count > 1


def check_unique(nums):
    """C-1.15
    Write a Python function that takes a sequence of numbers and determines
    if all the numbers are different from each other (that is, they are
    distinct).
    """
    return len(nums) == len(set(nums))


def scale16():
    """C-1.16
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
    return True


def scale17(data, factor):
    """C-1.17
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
    for val in data:
        val *= factor
    return data


def list_comp18():
    """C-1.18
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
    """
    return [x * (x+1) for x in range(10)]


def abc19():
    """C-1.19
    Demonstrate how to use Python’s list comprehension syntax to produce
    the list [ a , b , c , ..., z ], but without having to type all 26 such
    characters literally.
    """
    a_idx = 97
    return [chr(a_idx + x) for x in range(26)]


def rand_shuffle(test_list):
    """C-1.20
    Python’s random module includes a function shuffle(data) that accepts a
    list of elements and randomly reorders the elements so that each possi-
    ble order occurs with equal probability. The random module includes a
    more basic function randint(a, b) that returns a uniformly random integer
    from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function.
    """
    # Implementing Fisher-Yates shuffle
    for idx in range(len(test_list)-1, 1, -1):
        n = random.randint(0, idx)  # Upper bound is inclusive
        test_list[idx], test_list[n] = test_list[n], test_list[idx]


def user_input():
    """C-1.21
    Write a Python program that repeatedly reads lines from standard input
    until an EOFError is raised, and then outputs those lines in reverse order
    (a user can indicate end of input by typing ctrl-D).
    """
    lines = []
    while True:
        try:
            line = input('Input a phrase, CTRL-D to exit:')
            lines.append(line)
        except EOFError:
            break
    lines.reverse()
    for line in lines:
        print(line)
    return lines


def dot_product(a, b):
    """C-1.22
    Write a short Python program that takes two arrays a and b of length n
    storing int values, and returns the dot product of a and b. That is, it
    returns an array c of length n such that c[i] = a[i] · b[i], for i = 0, .
    . . , n − 1.
    """
    return array('i', [x * y for x, y in zip(a, b)])


def out_of_bounds(test_list, idx, val):
    """C-1.23
    Give an example of a Python code fragment that attempts to write an ele-
    ment to a list based on an index that may be out of bounds. If that index
    is out of bounds, the program should catch the exception that results, and
    print the following error message:
    “Don’t try buffer overflow attacks in Python!”
    """
    try:
        test_list[idx] = val
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
    return test_list


def count_vowels(string):
    """C-1.24
    Write a short Python function that counts the number of vowels in a given
    character string.
    """
    count = 0
    vowel_list = list('aeiou')
    for char in string:
        if char in vowel_list:
            count += 1
    return count


def remove_punctuation(string):
    """C-1.25
    Write a short Python function that takes a string s, representing a
    sentence, and returns a copy of the string with all punctuation removed.
    For example, if given the string "Let s try, Mike.", this function would
    return "Lets try Mike".
    """
    punctuation_list = list('\'\".,;:?!-(){}[]')
    new_string = ''
    for char in string:
        if char not in punctuation_list:
            new_string += char
    return new_string


def correct_arithmetic():
    """C-1.26
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
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    c = int(input('Enter c:'))
    conditions = [
        'a + b == c',
        'a == b + c',
        'a - b == c',
        'a == b - c',
        'a * b == c',
        'a == b * c',
        'a / b == c',
        'a == b / c',
        'a // b == c',
        'a == b // c',
        'a % b == c',
        'a == b % c'
    ]
    for condition in conditions:
        try:                     # Handle divide-by-zero errors
            if eval(condition):  # eval() is considered unsafe to use
                return True
        except ZeroDivisionError:
            pass
    return False


def compute_factor(n):
    """C-1.27
    In Section 1.8, we provided three different implementations of a generator
    that computes factors of a given integer. The third of those
    implementations, from page 41, was the most efficient, but we noted that
    it did not yield the factors in increasing order. Modify the generator so
    that it reports factors in increasing order, while maintaining its general
    performance advantages.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The third implementation's running time is O(sqrt(n)).  The solution below
    provides a sorted list of factors, but doubles the number of loop
    iterations.  However, O(2 * sqrt(n)) is still O(sqrt(n)), as the convention
    is to drop constants when using big-Oh notation.
    """
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
        k = k + 1
    if k * k == n:
        yield k
    k = k - 1
    while k > 0:
        if n % k == 0:
            yield n // k
        k = k - 1


def p_norm(vector, p=2):
    """C-1.28
    Give an implementation of a function named norm such that norm(v, p)
    returns the p-norm value of v and norm(v) returns the Euclidean norm of v.
    You may assume that v is a list of numbers.
    """
    return sum([x ** p for x in vector]) ** (1/p)


# %% Project Exercises
def catdog(char_list):
    """P-1.29
    Write a Python program that outputs all possible strings formed by using
    the characters c , a , t , d , o , and g exactly once.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A permutation of n elements without repetition has n! possible
    permutations.  'Catdog' should have 6! = 720 unique permutations.  Use
    recursion to swap characters and produce every possible permutation.
    """
    str_container = []
    n = len(char_list)

    def permutations(chars, step=0):
        if step == n:
            str_container.append("".join(chars))
        for idx in range(step, n):
            c_copy = chars.copy()  # Pass copy to avoid swapping same list
            c_copy[idx], c_copy[step] = c_copy[step], c_copy[idx]
            permutations(c_copy, step+1)
    permutations(char_list)
    return str_container


def two_divider(num):
    """P-1.30
    Write a Python program that can take a positive integer greater than 2
    as input and write out the number of times one must repeatedly divide
    this number by 2 before getting a value less than 2.
    """
    if not isinstance(num, int) or (num < 3):
        raise ValueError
    return int(math.log(num, 2))


def make_change(charged, given):
    """P-1.31
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
    given, charged = Decimal(str(given)), Decimal(str(charged))
    assert given > charged, 'Insufficient or exact payment'
    float_dict = {
        '100_dollar': 100,
        '50_dollar':  50,
        '20_dollar':  20,
        '10_dollar':  10,
        '5_dollar':   5,
        '1_dollar':   1,
        'quarter':    0.25,
        'dime':       0.10,
        'nickel':     0.05,
        'penny':      0.01
    }
    currency_dict = {k: Decimal(str(v)) for k, v in float_dict.items()}
    change_dict = {}
    expected_change = given - charged
    change_returned = Decimal(str('0'))
    for currency, value in currency_dict.items():
        while expected_change - change_returned >= value:
            change_returned += value
            change_dict[currency] = change_dict.get(currency, 0) + 1
    change_dict['Total change'] = f'${change_returned:,.2f}'
    return change_dict


def simple_calculator():
    """P-1.32
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
    def formatted_total(x):
        """Format number of decimal places for total."""
        if float(x).is_integer():
            return f'= {int(x)}'
        stringx = str(x)
        decimal = stringx.split('.')[-1]
        if len(decimal) < 5:
            return f'= {x}'
        return f'= {x:0.4f}'

    def is_number(string):
        """Alternative to isnumeric() that works for strings of floats."""
        try:
            float(string)
            return True
        except ValueError:
            return False

    def calculate(history):
        """Iterate through history of key presses and calculate the total."""
        val1 = None
        val2 = None
        total = 0
        for idx, val in enumerate(history):
            if is_number(val):
                if not val1:
                    val1 = val
                else:
                    val2 = val
            if val1 is not None and val2 is not None:
                if history[idx-1] == '+':
                    total = float(val1) + float(val2)
                if history[idx-1] == '-':
                    total = float(val1) - float(val2)
                if history[idx-1] == '*':
                    total = float(val1) * float(val2)
                if history[idx-1] == '/':
                    total = float(val1) / float(val2)
                val1 = total
                val2 = None
        print(formatted_total(total))

    operator_list = ['+', '-', '/', '*']
    button_history = []
    done = False
    print('Type "q" to quit')
    while not done:
        button = input('<Calc> ')
        if is_number(button) and len(button_history) == 0:
            button_history.append(button)
            print(button)
        elif (is_number(button) and (button_history[-1] in operator_list)) or\
                ((button in operator_list) and is_number(button_history[-1])):
            button_history.append(button)
            print(button)
        elif button == '=' and is_number(button_history[-1]):
            calculate(button_history)
            button_history.clear()
        elif button == 'q':
            done = True
        else:
            print('Invalid input!')


def handheld_calculator():
    """P-1.33
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
    def formatted_total(x):
        """Format number of decimal places for total."""
        if float(x).is_integer():
            return f'= {int(x)}'
        stringx = str(x)
        decimal = stringx.split('.')[-1]
        if len(decimal) < 5:
            return f'= {x}'
        return f'= {x:0.4f}'

    def is_number(string):
        """Alternative to isnumeric() that works for strings of floats."""
        try:
            float(string)
            return True
        except ValueError:
            return False

    def calculate(history):
        """Iterate through history of key presses and calculate the total."""
        val1 = None
        val2 = None
        total = 0
        for idx, val in enumerate(history):
            if is_number(val):
                if not val1:
                    val1 = val
                else:
                    val2 = val
            if val1 is not None and val2 is not None:
                if history[idx-1] == '+':
                    total = float(val1) + float(val2)
                if history[idx-1] == '-':
                    total = float(val1) - float(val2)
                if history[idx-1] == '*':
                    total = float(val1) * float(val2)
                if history[idx-1] == '/':
                    total = float(val1) / float(val2)
                val1 = total
                val2 = None
        print(formatted_total(total))
        return total

    operator_list = ['+', '-', '/', '*']
    button_history = []
    done = False
    print('Type "q" to quit')
    while not done:
        button = input('<Calc> ')
        if is_number(button) and len(button_history) == 0:
            button_history.append(button)
            print(button)
        elif (button in operator_list) and len(button_history) == 0:
            print('Invalid input!')
        elif (is_number(button) and (button_history[-1] in operator_list)) or\
                ((button in operator_list) and is_number(button_history[-1])):
            button_history.append(button)
            print(button)
        elif button == '=' and is_number(button_history[-1]):
            total = calculate(button_history)
            button_history = [total]
        elif button == 'cls':
            button_history.clear()
        elif button == 'q':
            done = True
        else:
            print('Invalid input!')


def punishment():
    """P-1.34
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
    sentence = "I will never spam my friends again."
    sentences = [sentence] * 100
    indices = random.sample(range(100), 8)
    for idx in indices:
        idx = int(idx)  # Avoid E1126 false positive from pylint
        done = False
        while not done:
            swap1, swap2 = random.sample(range(len(sentence)), 2)
            swap1, swap2 = int(swap1), int(swap2)  # Avoid E1126
            temp = list(sentences[idx])
            temp[swap1], temp[swap2] = temp[swap2], temp[swap1]
            temp_string = ''.join(temp)
            if temp_string not in sentences:
                sentences[idx] = temp_string
                done = True
    return [f'{x}. ' + words for x, words in zip(range(1, 101), sentences)]


def birthday_paradox(n, num_trials=10000):
    """P-1.35
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
    days = list(range(1, 366)) * 4
    days.append(366)
    same_bday_count = 0
    for _ in range(num_trials):
        birthdays = random.choices(days, k=n)
        if len(set(birthdays)) < len(birthdays):
            same_bday_count += 1
    return same_bday_count / num_trials


def count_words(sentence):
    """P-1.36
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
    word_list = sentence.split(' ')
    cleaned_words = [remove_punctuation(x).lower() for x in word_list]
    word_dict = {}
    for word in cleaned_words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict
