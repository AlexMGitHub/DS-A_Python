#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 5 exercises.

###############################################################################
# chapter5_exercises.py
#
# Revision:     1.00
# Date:         6/29/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 5 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports


# %% Reinforcement Exercises
def sum_matrix(list2d):
    """Solution to exercise R-5.11.

    Use standard control structures to compute the sum of all numbers in an
    n × n data set, represented as a list of lists.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I will create an nxn array, the values of which range from 1 to n^2.  The
    sum of this matrix then is the sum of the first n^2 integers.  The formula
    to calculate this sum is then: n^2 * (n^2 + 1) / 2.
    This will allow me to verify that my solution works as expected.
    """
    total = 0
    for row in list2d:
        for element in row:
            total += element
    return total


def sum_matrix2(list2d):
    """Solution to exercise R-5.12.

    Describe how the built-in sum function can be combined with Python’s
    comprehension syntax to compute the sum of all numbers in an n × n data
    set, represented as a list of lists.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I use a generator comprehension to save memory, as I am only interested in
    the resulting sum after iterating through all of the values in the matrix.
    The inner sum() function sums each list representing a row in the matrix,
    and the outer sum() function sums these sums, giving the final sum.
    """
    return sum(sum(row) for row in list2d)


# %% Project Exercises
class Matrix:
    """Solution to exercise P-5.33.

    Write a Python program for a matrix class that can add and multiply two-
    dimensional arrays of numbers, assuming the dimensions agree
    appropriately for the operation.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I used Python's dunder methods to overload the '+' and '@' operators for
    addition and matrix multiplication, respectively.  I also used the
    __getitem__ and __setitem__ dunder methods to allow the user to access the
    matrix values via 2D index.  Finally, I created representations of the
    Matrix() object using the __repr__ and __str__ dunder methods.
    """

    def __init__(self, matrix):
        """Accept a 2D list of lists and calculates its shape."""
        self._matrix = matrix
        self._rows = len(matrix)
        self._cols = len(matrix[0])

    def __add__(self, other):
        """Perform matrix addition if matrices have compatible dimensions."""
        assert self._rows == other._rows, 'Matrix dimensions not compatible'
        assert self._cols == other._cols, 'Matrix dimensions not compatible'
        new_mat = [[0] * self._cols for j in range(self._rows)]
        for i, row in enumerate(self._matrix):
            for j, element in enumerate(row):
                new_mat[i][j] = element + other._matrix[i][j]
        return Matrix(new_mat)

    def __matmul__(self, other):
        """Perform matrix multiplication if dimensions are compatible."""
        assert self._cols == other._rows, 'Matrix dimensions not compatible'
        new_mat = [[0] * other._cols for j in range(self._rows)]
        for row in range(self._rows):
            for col in range(other._cols):
                total = 0
                for k in range(self._cols):
                    total += self._matrix[row][k] * other._matrix[k][col]
                new_mat[row][col] = total
        return Matrix(new_mat)

    def __getitem__(self, idx_tup):
        """Return data located at (row, column) indices."""
        row_idx, col_idx = idx_tup
        return self._matrix[row_idx][col_idx]

    def __setitem__(self, idx_tup, value):
        """Set data located at (row, column) indices to supplied value."""
        row_idx, col_idx = idx_tup
        self._matrix[row_idx][col_idx] = value

    def __repr__(self):
        """Matrix representation defined as class and instance variables."""
        return str(self.__class__) + ", " + str(self.__dict__)

    def __str__(self):
        """Representation of 2D list formatted for pretty printing."""
        output = ['[']
        for row in self._matrix:
            output.append(str(row))
            output.append(',\n ')
        output.pop()  # Remove last comma and newline
        output.append(']')
        return ''.join(output)
