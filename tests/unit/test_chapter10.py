#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 10 exercises.

###############################################################################
# test_chapter10.py
#
# Revision:     1.00
# Date:         7/7/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 10 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports
import pytest

# Local application/library specific imports
import dsa.chapter10_exercises as chap10
from textbook_src.ch07.positional_list import PositionalList
from textbook_src.ch07.doubly_linked_base import _DoublyLinkedBase


# %% Reinforcement Exercises
def test_mutable_map_pop():
    """Solution to exercise R-10.1.

    Give a concrete implementation of the pop method in the context of the
    MutableMapping class, relying only on the five primary abstract methods
    of that class.
    """
    # Instantiate map and add key-value pairs
    my_map = chap10.MapConcrete()
    keys = 'abcdef'
    vals = [1, 2, 3, 4, 5, 6]
    for k, v in zip(keys, vals):
        my_map[k] = v
    # Test popping existing keys
    for k, v in zip(keys, vals):
        assert my_map.pop(k, 99) == v      # Default value should be ignored
    # Test pop operations on keys that don't exist
    with pytest.raises(KeyError):
        my_map.pop('x')
    assert my_map.pop('y', 99) == 99


def test_mutable_map_iter():
    """Solution to exercise R-10.2.

    Give a concrete implementation of the items( ) method in the context of
    the MutableMapping class, relying only on the five primary abstract
    methods of that class. What would its running time be if directly
    applied to the UnsortedTableMap subclass?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The __getitem__ method of the UnsortedTableMap class uses a for loop to
    scan the underlying list of items for a matching key, running in O(n)
    time.

    The items() method uses a tuple comprehension that calls __getitem__
    once for each of the n items in the list.  The run time of items() when
    applied to the UnsortedTableMap class is thus O(n^2).
    """
    # Instantiate map and add key-value pairs
    my_map = chap10.MapConcrete()
    keys = 'abcdef'
    vals = [1, 2, 3, 4, 5, 6]
    expected_items = []
    for k, v in zip(keys, vals):
        my_map[k] = v
        expected_items.append((k, v))
    # Return items and ensure that they match expectations
    items = set(my_map.items())  # Catch any duplicates by using set
    assert len(items) == len(expected_items)
    for item in items:
        assert item in expected_items


def test_unsorted_map_iter():
    """Solution to exercise R-10.3.

    Give a concrete implementation of the items( ) method directly within the
    UnsortedTableMap class, ensuring that the entire iteration runs in O(n)
    time.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    As noted in the solution to the previous problem, the UnsortedTableMap's
    __getitem__ method runs in O(n) time, and so if it is used by the iter()
    method the result will be O(n^2) time.

    One way to make iter() run in O(n) time is to simply bypass the __getitem__
    method and directly iterate through the _table variable storing the list of
    items.  I created an items2() method to do this.
    """
    # Instantiate map and add key-value pairs
    my_map = chap10.MapConcrete()
    keys = 'abcdef'
    vals = [1, 2, 3, 4, 5, 6]
    expected_items = []
    for k, v in zip(keys, vals):
        my_map[k] = v
        expected_items.append((k, v))
    # Return items and ensure that they match expectations
    items = set(my_map.items2())  # Catch any duplicates by using set
    assert len(items) == len(expected_items)
    for item in items:
        assert item in expected_items


def test_worst_case_running_time():
    """Solution to exercise R-10.4.

    What is the worst-case running time for inserting n key-value pairs into an
    initially empty map M that is implemented with the UnsortedTableMap
    class?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The UnsortedTableMap's __setitem__ method uses a for loop to check each
    item in the list for a matching key, and if none is found it will then add
    the new item to the list.

    Worst case, if all of the items have unique keys, then there will be n new
    items added, which will require searching a list that grows as 1 + 2 + 3 +
    ... + n-3 + n-2 + n-1.  This is the familiar sum of the first n integers,
    and so the worst-case run-time will be O(n^2).
    """
    assert chap10.worst_case_running_time()


def test_linked_list_map():
    """Solution to Exercise R-10.5.

    Reimplement the UnsortedTableMap class from Section 10.1.5, using the
    PositionalList class from Section 7.4 rather than a Python list.
    """
    # Instantiate map and add key-value pairs
    my_map = chap10.LinkedListMap()
    keys = 'abcdef'
    vals = [1, 2, 3, 4, 5, 6]
    expected_items = []
    for k, v in zip(keys, vals):
        my_map[k] = v
        expected_items.append((k, v))
    # Return items and ensure that they match expectations
    items = set(my_map.items())  # Catch any duplicates by using set
    assert len(items) == len(expected_items)
    for item in items:
        assert item in expected_items
    # Test that deletion works as expected
    del my_map['a']
    with pytest.raises(KeyError):
        my_map['a']
    with pytest.raises(KeyError):
        del my_map['a']
    my_map['b'] = 11
    assert my_map['b'] == 11


def test_load_factor():
    """Solution to Exercise R-10.6.

    Which of the hash table collision-handling schemes could tolerate a load
    factor above 1 and which could not?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    1. Separate chaining can handle a load factor above 1.  Although it will
       cause collisions and reduce run-time efficiency, the bucket array can
       handle multiple key-value pairs per cell.

    2. Open addressing schemes such as linear probing, quadratic probing, and
       double hashing cannot handle a load factor above 1.  These schemes
       require that there be an open cell to receive the new key-value pair,
       and a load factor of 1 means that all cells are occupied.
    """
    assert chap10.load_factor()


def test_position_hash():
    """Solution to exercise R-10.7.

    Our Position classes for lists and trees support the eq method so that
    two distinct position instances are considered equivalent if they refer to
    the same underlying node in a structure. For positions to be allowed as
    keys in a hash table, there must be a definition for the hash method that
    is consistent with this notion of equivalence. Provide such a hash
    method.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The Position class's eq method returns True if the positions being compared
    refer to the same node object.  This means that the hash of a position
    must return the hash of the memory address of the node that the position
    refers to.  This way if position_x == position_y, then hash(position_x) ==
    hash(position_y).

    I obtain the memory address of the position's node using Python's id()
    built-in function, which returns an integer that is guaranteed to be
    unique for the object during its lifetime.  An integer is a hashable
    object, and so this should meet the requirements stated in the exercise.
    """
    container = PositionalList()
    node_x = _DoublyLinkedBase._Node(0, 0, 0)  # Initialize with garbage
    node_z = _DoublyLinkedBase._Node(0, 0, 0)  # Initialize with garbage
    pos_x = chap10.HashablePosition(container, node_x)  # Init with node_x
    pos_y = chap10.HashablePosition(container, node_x)  # Same node as pos_x
    pos_z = chap10.HashablePosition(container, node_z)  # Init with node_z
    # Check equality between positions
    assert pos_x == pos_y  # Position refer to same node (node_x)
    assert pos_x != pos_z  # Positions refer to different node (node_x, node_z)
    # Check equality between hash codes
    assert hash(pos_x) == hash(pos_y)  # Hash codes of same node
    assert hash(pos_x) != hash(pos_z)  # Hash codes of different nodes


def test_vehicle_id_hash():
    """Solution to exercise R-10.8.

    What would be a good hash code for a vehicle identification number that
    is a string of numbers and letters of the form “9X9XX99X9XX999999,”
    where a “9” represents a digit and an “X” represents a letter?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The vehicle identification number is a sequence of integers and characters
    where the order of the sequence matters, e.g. 9X9X != 99XX.

    From the text, such sequences are suitable for hashing using a polynomial
    hash code or a cyclic-shift hash code.

    The characters can be represented by their Unicode values, resulting in a
    tuple of integers of the form (x0, x1, ..., x_n-1).  Integers are 32-bits
    in Python, as are hash codes, so this lends itself well to either the
    polynomial or cyclic-shift methods.

    Whichever method is chosen, there will need to be fine-tuning to determine
    the optimal number of bits to shift or the optimal value for "a".
    """
    assert chap10.vehicle_id_hash()


def test_chaining():
    """Solution to exercise R-10.9.

    Draw the 11-entry hash table that results from using the hash function,
    h(i) = (3i + 5) mod 11, to hash the keys 12, 44, 13, 88, 23, 94, 11, 39,
    20, 16, and 5, assuming collisions are handled by chaining.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Indices:       0  1  2  3  4  5  6  7  8  9  10
    0. Initial:   [[],[],[],[],[],[],[],[],[],[],[]]
    1. h(12) = 8  [[],[],[],[],[],[],[],[],[12],[],[]]
    2. h(44) = 5  [[],[],[],[],[],[44],[],[],[12],[],[]]
    3. h(13) = 0  [[13],[],[],[],[],[44],[],[],[12],[],[]]
    4. h(88) = 5  [[13],[],[],[],[],[44,88],[],[],[12],[],[]]
    5. h(23) = 8  [[13],[],[],[],[],[44,88],[],[],[12,23],[],[]]
    6. h(94) = 1  [[13],[94],[],[],[],[44,88],[],[],[12,23],[],[]]
    7. h(11) = 5  [[13],[94],[],[],[],[44,88,11],[],[],[12,23],[],[]]
    8. h(39) = 1  [[13],[94,39],[],[],[],[44,88,11],[],[],[12,23],[],[]]
    9. h(20) = 10 [[13],[94,39],[],[],[],[44,88,11],[],[],[12,23],[],[20]]
    10. h(16) = 9 [[13],[94,39],[],[],[],[44,88,11],[],[],[12,23],[16],[20]]
    11. h(5) = 9  [[13],[94,39],[],[],[],[44,88,11],[],[],[12,23],[16,5],[20]]
    """
    keys = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    entries = [[13], [94, 39], [], [], [], [
        44, 88, 11], [], [], [12, 23], [16, 5], [20]]
    hash_table = chap10.SimpleChainHashTable()
    for key in keys:
        hash_table[key] = key               # Insert keys
    assert len(hash_table) == 11
    for idx, bucket in enumerate(hash_table):
        assert entries[idx] == bucket       # Compare entries to expected
    # Test SimpleHashTable methods
    with pytest.raises(KeyError):
        del hash_table[3]                   # Deleted key does not exist
    hash_table[12] = 999
    assert hash_table[12] == 999            # Test modifying keys
    del hash_table[12]
    with pytest.raises(KeyError):
        hash_table[12]                      # Verify key is deleted
    assert len(hash_table) == 10


def test_linear_probing():
    """Solution to exercise R-10.10.

    What is the result of the previous exercise, assuming collisions are han-
    dled by linear probing?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    If a collision occurs, linear probing will increment the index as
    (j+1) % N until an empty slot is found or we wrap around to the original
    index.  Deleted items must be replaced with an AVAILABLE sentinel.

    Indices:       0  1  2  3  4  5  6  7  8  9  10
    0. Initial:   [ , , , , , , , , , , ]
    1. h(12) = 8  [ , , , , , , , , 12, , ]
    2. h(44) = 5  [ , , , , , 44, , , 12, , ]
    3. h(13) = 0  [13, , , , , 44, , , 12, , ]
    4. h(88) = 5  [13, , , , , 44, 88, , 12, , ]
    5. h(23) = 8  [13, , , , , 44, 88, , 12, 23, ]
    6. h(94) = 1  [13, 94, , , , 44, 88, , 12, 23, ]
    7. h(11) = 5  [13, 94, , , , 44, 88, 11, 12, 23, ]
    8. h(39) = 1  [13, 94, 39, , , 44, 88, 11, 12, 23, ]
    9. h(20) = 10 [13, 94, 39, , , 44, 88, 11, 12, 23, 20]
    10. h(16) = 9 [13, 94, 39, 16, , 44, 88, 11, 12, 23, 20]
    11. h(5) = 9  [13, 94, 39, 16, 5, 44, 88, 11, 12, 23, 20]
    """
    keys = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    entries = [13, 94, 39, 16, 5, 44, 88, 11, 12, 23, 20]
    hash_table = chap10.SimpleLinearProbeHashTable()
    # Test operations on empty hash table
    with pytest.raises(KeyError):
        hash_table[11]                      # Accessing empty table
    with pytest.raises(KeyError):
        del hash_table[11]                  # Deleting item in empty table
    for _ in hash_table:
        pass                                # Iterate over empty table
    # Verify solution to exercise
    for key in keys:
        hash_table[key] = key               # Insert keys
    assert len(hash_table) == 11
    for idx, bucket in enumerate(hash_table):
        assert entries[idx] == bucket       # Compare entries to expected
    # Test SimpleHashTable methods
    assert hash_table[13] == 13             # Valid key
    with pytest.raises(KeyError):
        hash_table[111] = 222               # Table is full
    with pytest.raises(KeyError):
        hash_table[3]                       # Accessed key does not exist
    with pytest.raises(KeyError):
        del hash_table[3]                   # Deleted key does not exist
    hash_table[12] = 999
    assert hash_table[12] == 999            # Test modifying keys
    del hash_table[12]
    with pytest.raises(KeyError):
        hash_table[12]                      # Verify key is deleted
    assert len(hash_table) == 10
    assert hash_table[5] == 5
    del hash_table[5]
    assert len(hash_table) == 9
    hash_table[11] = 7
    assert len(hash_table) == 9


def test_quadratic_probing():
    """Solution to exercise R-10.11.

    Show the result of Exercise R-10.9, assuming collisions are handled by
    quadratic probing, up to the point where the method fails.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    If a collision occurs, quadratic probing will increment the index as
    (j+f(i)) % N until an empty slot is found or we wrap around to the original
    index.  Deleted items must be replaced with an AVAILABLE sentinel.

    Indices:       0  1  2  3  4  5  6  7  8  9  10
    0. Initial:   [ , , , , , , , , , , ]
    1. h(12) = 8  [ , , , , , , , , 12, , ]
    2. h(44) = 5  [ , , , , , 44, , , 12, , ]
    3. h(13) = 0  [13, , , , , 44, , , 12, , ]
    4. h(88) = 5  [13, , , , , 44, 88, , 12, , ]
    5. h(23) = 8  [13, , , , , 44, 88, , 12, 23, ]
    6. h(94) = 1  [13, 94, , , , 44, 88, , 12, 23, ]
    7. h(11) = 5  [13, 94, , 11, , 44, 88, , 12, 23, ]
    8. h(39) = 1  [13, 94, 39, 11, , 44, 88, , 12, 23, ]
    9. h(20) = 10 [13, 94, 39, 11, , 44, 88, , 12, 23, 20]
    10. h(16) = 9 [13, 94, 39, 11, , 44, 88, 16, 12, 23, 20]
    11. h(5) = 9  No valid index for i in range [0, N-1]
    """
    keys = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    entries = (13, 94, 39, 11, None, 44, 88, 16, 12, 23, 20)
    hash_table = chap10.SimpleQuadraticProbeHashTable()
    # Test operations on empty hash table
    with pytest.raises(KeyError):
        hash_table[11]                      # Accessing empty table
    with pytest.raises(KeyError):
        del hash_table[11]                  # Deleting item in empty table
    for _ in hash_table:
        pass                                # Iterate over empty table
    # Verify solution to exercise
    for key in keys:
        try:
            hash_table[key] = key           # Insert keys
        except TypeError:
            continue                        # Unable to fill index 4
    assert len(hash_table) == 10            # Table not completely filled
    for idx, bucket in enumerate(hash_table):
        assert entries[idx] == bucket       # Compare entries to expected
    hash_table[23] = 101
    assert hash_table[23] == 101            # Test modifying values of key
    with pytest.raises(KeyError):
        hash_table[555]                     # Key doesn't exist
    hash_table._table[4] = (5, 5)           # Manually place item in slot 4
    with pytest.raises(KeyError):
        hash_table[545]                     # Check _find_key() condition


def test_secondary_hashing():
    """Solution to exercise R-10.12.

    What is the result of Exercise R-10.9 when collisions are handled by dou-
    ble hashing using the secondary hash function h'(k) = 7 − (k mod 7)?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    If a collision occurs, secondary hashing will increment the index as
    (j+f(i)) % N until an empty slot is found or we wrap around to the original
    index.  Deleted items must be replaced with an AVAILABLE sentinel.

    Indices:       0  1  2  3  4  5  6  7  8  9  10
    0. Initial:   [ , , , , , , , , , , ]
    1. h(12) = 8  [ , , , , , , , , 12, , ]
    2. h(44) = 5  [ , , , , , 44, , , 12, , ]
    3. h(13) = 0  [13, , , , , 44, , , 12, , ]
    4. h(88) = 5  [13, , , 88, , 44, , , 12, , ]
    5. h(23) = 8  [13, , 23, 88, , 44, , , 12, , ]
    6. h(94) = 1  [13, 94, 23, 88, , 44, , , 12, , ]
    7. h(11) = 5  [13, 94, 23, 88, , 44, 11, , 12, , ]
    8. h(39) = 1  [13, 94, 23, 88, 39, 44, 11, , 12, , ]
    9. h(20) = 10 [13, 94, 23, 88, 39, 44, 11, , 12, , 20]
    10. h(16) = 9 [13, 94, 23, 88, 39, 44, 11, , 12, 16, 20]
    11. h(5) = 9  [13, 94, 23, 88, 39, 44, 11, 5, 12, 16, 20]
    """
    keys = (12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5)
    entries = [13, 94, 23, 88, 39, 44, 11, 5, 12, 16, 20]
    hash_table = chap10.SimpleSecondaryHashTable()
    # Test operations on empty hash table
    with pytest.raises(KeyError):
        hash_table[11]                      # Accessing empty table
    with pytest.raises(KeyError):
        del hash_table[11]                  # Deleting item in empty table
    for _ in hash_table:
        pass                                # Iterate over empty table
    # Verify solution to exercise
    for key in keys:
        hash_table[key] = key               # Insert keys
    assert len(hash_table) == 11
    for idx, bucket in enumerate(hash_table):
        assert entries[idx] == bucket       # Compare entries to expected
    # Test SimpleHashTable methods
    assert hash_table[13] == 13             # Valid key
    with pytest.raises(KeyError):
        hash_table[111] = 222               # Table is full
    with pytest.raises(KeyError):
        hash_table[3]                       # Accessed key does not exist
    with pytest.raises(KeyError):
        del hash_table[3]                   # Deleted key does not exist
    hash_table[12] = 999
    assert hash_table[12] == 999            # Test modifying keys
    del hash_table[12]
    with pytest.raises(KeyError):
        hash_table[12]                      # Verify key is deleted
    assert len(hash_table) == 10
    assert hash_table[5] == 5
    del hash_table[5]
    assert len(hash_table) == 9
    hash_table[11] = 7
    assert len(hash_table) == 9


def test_worst_case_chaining():
    """Solution to exercise R-10.13.

    What is the worst-case time for putting n entries in an initially empty
    hash table, with collisions resolved by chaining? What is the best case?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The worst case occurs when all n entries are hashed to the same bucket.
    As stated in the text, the operations on an individual bucket take time
    proportional to the size of the bucket, assuming the bucket is unsorted.
    This is because each time an element is added to the bucket, its key must
    be compared to all other existing items in the bucket.  If n items are
    added to the same bucket, then we have the familiar sum of the first n-1
    integers as the number of comparisons increases by 1 for each added item.
    Therefore the worst-case for operations for separate chaining is O(n^2).

    In the best case, each of the n entries will hash to a separate bucket.
    According to the text, when the load factor lambda is O(1) the core
    operations on the hash table run in O(1) time.  If each item hashed to a
    unique index in the array, then we know that N is at least equal to n, and
    thus the load factor is O(1) and the operations are O(1).  As we must
    perform n O(1) operations to add n entries to the hash table, the
    best-case time is O(n).
    """
    assert chap10.worst_case_chaining()


def test_rehash_fig_10p6():
    """Solution to exercise R-10.14.

    Show the result of rehashing the hash table shown in Figure 10.6 into a
    table of size 19 using the new hash function h(k) = 3k mod 17.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Note that the new hash function is mod 17, while the table is of size 19.
    I am assuming that for the purpose of this exercise I should not apply a
    compression function.

    1. h(54) = 9
    2. h(28) = 16
    3. h(41) = 4
    4. h(18) = 3
    5. h(10) = 13
    6. h(36) = 6
    7. h(25) = 7
    8. h(38) = 12
    9. h(12) = 2
    10. h(90) = 15

     0  1   2   3   4  5   6   7  8   9  10  11  12  13  14  15  16  17  18
    ( ,  , 12, 18, 41,  , 36, 25,  , 54,  ,   ,  38, 10,   , 90, 28,  ,   ,)
    """
    keys = (54, 28, 41, 18, 10, 36, 25, 38, 12, 90)
    solution = ([], [], [12], [18], [41], [], [36], [25], [],
                [54], [], [], [38], [10], [], [90], [28], [], [])
    hash_table = chap10.SimpleChainHashTableP14()
    # Add entries to hash table
    for key in keys:
        hash_table[key] = key
    # Verify hash table matches expectation
    for entry, expected in zip(hash_table, solution):
        assert entry == expected


def test_not_suited():
    """Solution to exercise R-10.18.

    Explain why a hash table is not suited to implement a sorted map.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Hash tables perform exact searches.  A hash table can quickly determine if
    an item with a given key exists in the table.  However, it scatters these
    keys throughout the hash table in order to ensure fast performance.
    The keys are thus not arranged in some sort of order determined by their
    relationship to other keys.

    A sorted map relies on a binary search to efficiently perform inexact
    searches.  A binary search requires the keys to be sorted, which cannot
    occur in an efficient implementation of a hash table.
    """
    assert chap10.not_suited()


def test_worst_case_asymp_running_time():
    """Solution to exercise R-10.20.

    What is the worst-case asymptotic running time for performing n deletions
    from a SortedTableMap instance that initially contains 2n entries?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Deleting an item in the SortedTableMap requires two operations:
    1. Finding the index associated with the key
    2. Popping the index from the underlying list

    Finding the index is performed using a binary search, which executes in
    O(logn) time.  Since there are 2n items, this would be O(log2n) time.

    Popping an item from the list is worst case O(n), because all of the other
    elements in the list must be shifted.  Since there are 2n items, this
    would be O(2n) time.

    We are deleting n of 2n items in a map, and so both of these operations
    are called n times.  As the items are deleted, the length of the map
    will decrease from 2n to n.  This means that the searches and deletions
    will grow faster as items are deleted, but they will still be log/linear
    with n as there will always be at least n items in the map.

    This simplifies the analysis of the run-time efficiency to:

    n * (2n + log2n) = 2n^2 + nlog2n

    Big-O notation ignores constants and only considers the dominant term,
    and so the worst-case asymptotic running time for performing n deletions is
    O(n^2).  Table 10.3 in the text lists the delete operation as being worst
    case O(n), and so n deletions would be O(n^2).  This appears to support the
    conclusion stated above.
    """
    assert chap10.worst_case_asymp_running_time()
