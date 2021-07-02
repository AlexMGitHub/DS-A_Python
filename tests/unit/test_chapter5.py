#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 5 exercises.

###############################################################################
# test_chapter5.py
#
# Revision:     1.00
# Date:         6/29/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 5 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports
import pytest
import numpy as np

# Local application/library specific imports
import dsa.chapter5_exercises as chap5


# %% Reinforcement Exercises
def test_sum_matrix():
    """Solution to exercise R-5.11.

    Use standard control structures to compute the sum of all numbers in an
    n × n data set, represented as a list of lists.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I will create an (n x n) array, the values of which range from 1 to n^2.
    The sum of this matrix then is the sum of the first n^2 integers.
    The formula to calculate this sum is then: n^2 * (n^2 + 1) / 2.
    This will allow me to verify that my solution works as expected.
    """
    n = 10
    alist = [[i for i in range(1+n*j, n*(j+1)+1)] for j in range(0, n)]
    expected_result = n**2 * (n**2 + 1) / 2
    result = chap5.sum_matrix(alist)
    assert result == expected_result


def test_sum_matrix2():
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
    n = 10
    alist = [[i for i in range(1+n*j, n*(j+1)+1)] for j in range(0, n)]
    expected_result = n**2 * (n**2 + 1) / 2
    result = chap5.sum_matrix2(alist)
    assert result == expected_result


# %% Project Exercises
@pytest.fixture(name="matrices", scope="class")
def matrix_fixture():
    """Fixture to supply matrices to the TestMatrix() class."""
    class MatrixInit:
        """Fixture class to store matrices as instance variables."""

        def __init__(self):
            """Define matrices to be used for testing the Matrix() class."""
            n = 10  # Define a 10x10 square matrix
            self.n = n
            self.square = [[i for i in range(1+n*j, n*(j+1)+1)]
                           for j in range(0, n)]
            # Define 5x10 and 10x5 matrices
            self.half_row = [[i for i in range(1+n*j, n*(j+1)+1)]
                             for j in range(0, n//2)]
            self.half_col = [[i for i in range(1+n*j//2, n*(j+1)//2+1)]
                             for j in range(0, n)]
    return MatrixInit()


class TestMatrix:
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

    def test_add(self, matrices):
        """Test Matrix class __add__() method."""
        # Calculate the expected result of adding the square matrix to itself
        n = matrices.n
        add_result = [[2*i for i in range(1+n*j, n*(j+1)+1)]
                      for j in range(0, n)]
        # Instantiate the 10x10 matrices and test addition
        mat_a = chap5.Matrix(matrices.square)
        mat_b = chap5.Matrix(matrices.square)
        square_add = mat_a + mat_b
        assert square_add._matrix == add_result
        # Instantiate a 5x10 and 10x5 matrix as Matrix class and Numpy array
        half_row_mat = chap5.Matrix(matrices.half_row)
        half_col_mat = chap5.Matrix(matrices.half_col)
        half_row_np = np.array(matrices.half_row)
        half_col_np = np.array(matrices.half_col)
        # Adding half matrices to themselves and compare to Numpy results
        half_row_add = (half_row_mat + half_row_mat)._matrix
        half_col_add = (half_col_mat + half_col_mat)._matrix
        assert (np.array(half_row_add) == half_row_np + half_row_np).all()
        assert (np.array(half_col_add) == half_col_np + half_col_np).all()

    def test_matmul(self, matrices):
        """Test Matrix class __matmul__() method."""
        # Instantiate the 10x10 matrix and test matrix multiplication
        square_mat = chap5.Matrix(matrices.square)
        square_np = np.array(matrices.square)
        square_matmul = (square_mat @ square_mat)._matrix
        square_np_result = square_np @ square_np
        # Compare to the Numpy result of multiplying the matrix times itself
        assert (np.array(square_matmul) == square_np_result).all()
        # Instantiate a 5x10 and 10x5 matrix as Matrix class and Numpy array
        half_row_mat = chap5.Matrix(matrices.half_row)
        half_col_mat = chap5.Matrix(matrices.half_col)
        half_row_np = np.array(matrices.half_row)
        half_col_np = np.array(matrices.half_col)
        # Matrix multiplication amongst the 10x10, 5x10, and 10x5 matrices
        result1 = half_row_mat @ half_col_mat       # (5x10)  @ (10x5)
        exp_result1 = half_row_np @ half_col_np     # (5x10)  @ (10x5)
        result2 = half_col_mat @ half_row_mat       # (10x5)  @ (5x10)
        exp_result2 = half_col_np @ half_row_np     # (10x5)  @ (5x10)
        result3 = half_row_mat @ square_mat         # (5x10)  @ (10x10)
        exp_result3 = half_row_np @ square_np       # (5x10)  @ (10x10)
        result4 = square_mat @ half_col_mat         # (10x10) @ (10x5)
        exp_result4 = square_np @ half_col_np       # (10x10) @ (10x5)
        assert (np.array(result1._matrix) == exp_result1).all()
        assert (np.array(result2._matrix) == exp_result2).all()
        assert (np.array(result3._matrix) == exp_result3).all()
        assert (np.array(result4._matrix) == exp_result4).all()

    def test_incompatible_dimensions(self, matrices):
        """Test operations with incompatible matrix dimensions."""
        # Instantiate 5x10, 10x5, and 10x10 matrices as Matrix class
        square_mat = chap5.Matrix(matrices.square)
        half_row_mat = chap5.Matrix(matrices.half_row)
        half_col_mat = chap5.Matrix(matrices.half_col)
        # Verify Matrix class raises AssertionError for incompatible dimensions
        with pytest.raises(AssertionError):
            half_row_mat + half_col_mat         # (5x10) + (10x5)
        with pytest.raises(AssertionError):
            half_col_mat + half_row_mat         # (10x5) + (5x10)
        with pytest.raises(AssertionError):
            half_col_mat @ square_mat           # (10x5) @ (10x10)
        with pytest.raises(AssertionError):
            square_mat @ half_row_mat           # (10x10) @ (5x10)

    def test_indexing(self, matrices):
        """Test ability to access Matrix data with a 2D index."""
        # Test __getitem__ functionality
        n = matrices.n
        square_mat = chap5.Matrix(matrices.square)
        assert square_mat[(0, 0)] == 1
        # Test __setitem__ functionality
        square_mat[(n-1, n-1)] = -99
        assert square_mat[(n-1, n-1)] == -99

    def test_repr_str(self, matrices):
        """Test Matrix() __repr__ and __str__ methods."""
        square_mat = chap5.Matrix(matrices.square)
        # Test __repr__
        dict_items = ('Matrix', '_matrix', '_rows', '_cols')
        assert all(x in repr(square_mat) for x in dict_items)
        # Test __str__
        row_str = str(square_mat._matrix[0])
        assert row_str in str(square_mat)
