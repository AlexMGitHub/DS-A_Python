#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 2 exercises.

###############################################################################
# chapter2_exercises.py
#
# Revision:     1.00
# Date:         6/25/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 2 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports


# %% Reinforcement Exercises
def life_critical():
    """Solution to exercise R-2.1.

    Give three examples of life-critical software applications.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. Automatic braking of cars
    2. Computerized flight control
    3. Radiation therapy machines
    """
    return True


def adaptability():
    """Solution to exercise R-2.2.

    Give an example of a software application in which adaptability can mean
    the difference between a prolonged lifetime of sales and bankruptcy.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A social media app needs to be able to constantly evolve to keep up with
    trends and user features that are offered by their competitors.
    """
    return True


def text_editor():
    """Solution to exercise R-2.3.

    Describe a component from a text-editor GUI and the methods that it
    encapsulates.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The spellchecker is a common component in a text editor.  Its methods
    might include:
    1. run_spellcheck()
    2. parse_text()
    3. lookup_word()
    4. underline_misspelled_word()
    """
    return True


class Flower:
    """Solution to exercise R-2.4.

    Write a Python class, Flower, that has three instance variables of type
    str, int, and float, that respectively represent the name of the flower,
    its number of petals, and its price. Your class must include a constructor
    method that initializes each variable to an appropriate value, and your
    class should include methods for setting the value of each type, and
    retrieving the value of each type.
    """

    def __init__(self, name, num_petals, price):
        """Initialize instance of Flower class."""
        assert isinstance(name, str), 'Name must be string'
        assert isinstance(num_petals, int), 'Number of petals must be integer'
        assert isinstance(price, float), 'Price must be a float'
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def set_name(self, name):
        """Set name of the flower."""
        assert isinstance(name, str), 'Name must be string'
        self._name = name

    def get_name(self):
        """Return name of the flower."""
        return self._name

    def set_num_petals(self, num_petals):
        """Set flower's number of petals."""
        assert isinstance(num_petals, int), 'Number of petals must be integer'
        self._num_petals = num_petals

    def get_num_petals(self):
        """Return flower's number of petals."""
        return self._num_petals

    def set_price(self, price):
        """Set price of the flower."""
        assert isinstance(price, float), 'Price must be a float'
        self._price = price

    def get_price(self):
        """Return price of the flower."""
        return self._price


class CreditCard:
    """Solution to exercise R-2.5.

    Use the techniques of Section 1.7 to revise the charge and make payment
    methods of the CreditCard class to ensure that the caller sends a number
    as a parameter.
    """

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero.
        customer  the name of the customer (e.g., 'John Bowman')
        bank      the name of the bank (e.g., 'California Savings')
        acnt      the acount identifier (e.g., '5391 0375 9387 5309')
        limit     credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    # def get_customer(self):
    #     """Return name of the customer."""
    #     return self._customer

    # def get_bank(self):
    #     """Return the bank's name."""
    #     return self._bank

    # def get_account(self):
    #     """Return the card identifying number (typically stored as a string).
    #     """
    #     return self._account

    # def get_limit(self):
    #     """Return current credit limit."""
    #     return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be numeric')
        if price + self._balance > self._limit:  # if charge would exceed limit
            return False                         # cannot accept charge
        self._balance += price
        return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError('Amount must be numeric')
        self._balance -= amount
