#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 2 exercises.

###############################################################################
# test_chapter2.py
#
# Revision:     1.00
# Date:         6/25/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 2 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Related third party imports
import pytest

# Local application/library specific imports
import dsa.chapter2_exercises as chap2


# %% Reinforcement Exercises
def test_life_critical():
    """Solution to exercise R-2.1.

    Give three examples of life-critical software applications.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. Automatic braking of cars
    2. Computerized flight control
    3. Radiation therapy machines
    """
    assert chap2.life_critical()


def test_adaptability():
    """Solution to exercise R-2.2.

    Give an example of a software application in which adaptability can mean
    the difference between a prolonged lifetime of sales and bankruptcy.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A social media app needs to be able to constantly evolve to keep up with
    trends and user features that are offered by their competitors.
    """
    assert chap2.adaptability()


def test_text_editor():
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
    assert chap2.text_editor()


class TestFlower():
    """Solution to exercise R-2.4.

    Write a Python class, Flower, that has three instance variables of type
    str, int, and float, that respectively represent the name of the flower,
    its number of petals, and its price. Your class must include a constructor
    method that initializes each variable to an appropriate value, and your
    class should include methods for setting the value of each type, and
    retrieving the value of each type.
    """

    def test_instance(self):
        """Test basic functionality of a Flower instance."""
        flower = chap2.Flower('Iris', 8, 3.27)
        assert flower.get_name() == 'Iris'
        assert flower.get_num_petals() == 8
        assert flower.get_price() == 3.27
        flower.set_name('Petunia')
        flower.set_num_petals(6)
        flower.set_price(2.16)
        assert flower.get_name() == 'Petunia'
        assert flower.get_num_petals() == 6
        assert flower.get_price() == 2.16

    @pytest.mark.parametrize('name, num_petals, price',
                             [(99, 8, 3.27),
                              ('Iris', 8.5, 3.27),
                              ('Iris', 8, 2)
                              ])
    def test_constructor(self, name, num_petals, price):
        """Test type-checking of Flower constructor."""
        with pytest.raises(AssertionError):
            chap2.Flower(name, num_petals, price)

    @pytest.mark.parametrize('name, num_petals, price',
                             [(True, '6', False),
                              (5, 3.33, 'invalid'),
                              (3.2, 4.5, 5)
                              ])
    def test_setters(self, name, num_petals, price):
        """Test type-checking of Flower set methods."""
        flower = chap2.Flower('Iris', 8, 3.27)
        with pytest.raises(AssertionError):
            flower.set_name(name)
        with pytest.raises(AssertionError):
            flower.set_num_petals(num_petals)
        with pytest.raises(AssertionError):
            flower.set_price(price)


def test_credit_card():
    """Solution to exercise R-2.5.

    Use the techniques of Section 1.7 to revise the charge and make payment
    methods of the CreditCard class to ensure that the caller sends a number
    as a parameter.
    """
    cc = chap2.CreditCard('John Doe', '1st Bank', '5391 0375 9387 5309', 1000)
    assert cc.get_balance() == 0
    cc.charge(300)
    assert cc.get_balance() == 300
    cc.charge(15.50)
    assert cc.get_balance() == 315.50
    cc.make_payment(250)
    assert cc.get_balance() == (315.50 - 250)
    cc.make_payment(45.50)
    assert cc.get_balance() == 20
    with pytest.raises(TypeError):
        cc.charge('$5.00')
    with pytest.raises(TypeError):
        cc.make_payment('$10.00')
    assert not cc.charge(5000)
