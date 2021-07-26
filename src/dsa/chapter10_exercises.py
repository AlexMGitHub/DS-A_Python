#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 10 exercises.

###############################################################################
# chapter10_exercises.py
#
# Revision:     1.00
# Date:         7/7/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 10 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
from textbook_src.ch10.unsorted_table_map import UnsortedTableMap
from textbook_src.ch07.positional_list import PositionalList


# %% Reinforcement Exercises
class MapConcrete(UnsortedTableMap):
    """Solutions to problems requiring modificiation of MutableMap class."""

    def pop(self, k, d=None):
        """Solution to exercise R-10.1.

        Give a concrete implementation of the pop method in the context of the
        MutableMapping class, relying only on the five primary abstract methods
        of that class.
        """
        try:
            value = self[k]     # Attempt to get value associated with key
        except KeyError as key_err:
            if d is None:
                raise KeyError('Key Error: ' + repr(k)) from key_err
            return d            # Return specified default value
        del self[k]             # We know that key exists
        return value

    def items(self):
        """Solution to exercise R-10.2.

        Give a concrete implementation of the items( ) method in the context of
        the MutableMapping class, relying only on the five primary abstract
        methods of that class. What would its running time be if directly
        applied to the UnsortedTableMap subclass?

        -----------------------------------------------------------------------
        Solution:
        -----------------------------------------------------------------------
        The __getitem__ method of the UnsortedTableMap class uses a for loop to
        scan the underlying list of items for a matching key, running in O(n)
        time.

        The items() method uses a tuple comprehension that calls __getitem__
        once for each of the n items in the list.  The run time of items() when
        applied to the UnsortedTableMap class is thus O(n^2).
        """
        return ((k, self[k]) for k in self)

    def items2(self):
        """Solution to exercise R-10.3.

        Give a concrete implementation of the items( ) method directly within
        the UnsortedTableMap class, ensuring that the entire iteration runs in
        O(n) time.

        -----------------------------------------------------------------------
        Solution:
        -----------------------------------------------------------------------
        As noted in the solution to the previous problem, the
        UnsortedTableMap's __getitem__ method runs in O(n) time, and so if it
        is used by the iter() method the result will be O(n^2) time.

        One way to make iter() run in O(n) time is to simply bypass the
        __getitem__ method and directly iterate through the _table variable
        storing the list of items.  I created an items2() method to do this.
        """
        return ((item._key, item._value) for item in self._table)


def worst_case_running_time():
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
    return True


class LinkedListMap(UnsortedTableMap):
    """Solution to Exercise R-10.5.

    Reimplement the UnsortedTableMap class from Section 10.1.5, using the
    PositionalList class from Section 7.4 rather than a Python list.
    """

    def __init__(self):
        """Create an empty map."""
        self._table = PositionalList()  # Positional list of _Items

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:                          # Found a match:
                item._value = v                         # reassign value
                return                                  # and quit
        # did not find match for key
        self._table.add_last(self._Item(k, v))

    def _iter(self):
        """Generate a forward iteration of the positions of the list."""
        cursor = self._table.first()
        while cursor is not None:
            yield cursor
            cursor = self._table.after(cursor)

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for position in self._iter():
            if k == position.element()._key:            # Found a match
                self._table.delete(position)            # Remove position
                return                                  # and quit
        raise KeyError('Key Error: ' + repr(k))


def load_factor():
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
    return True


class HashablePosition(PositionalList.Position):
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

    def __hash__(self):
        """Return a hash code based on the memory address of the node."""
        return hash(id(self._node))


def vehicle_id_hash():
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
    return True


class SimpleChainHashTable:
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

    def __init__(self, cap=11):
        """Initialize a simple class with a subset of hash table methods."""
        self._cap = cap
        self._n = 0
        self._table = [[] for x in range(cap)]

    def __len__(self):
        """Return number of elements in hash table."""
        return self._n

    def __getitem__(self, k):
        """Return bucket located at index associated with key."""
        j = self._hash_function(k)
        for tup in self._table[j]:
            if k in tup:
                return tup[1]             # Return value of (k, v) tuple
        raise KeyError('Invalid key!')    # Key not found in bucket

    def __setitem__(self, k, v):
        """Add key-value pair to hash table.

        Overwrite the value of existing key.
        """
        j = self._hash_function(k)
        for idx, tup in enumerate(self._table[j]):
            if k in tup:                      # Key already exists in bucket
                self._table[j][idx] = (k, v)  # Update value of key-value pair
                return
        self._table[j].append((k, v))         # Else add key-value pair
        self._n += 1

    def __delitem__(self, k):
        """Delete key-value pair if it exists in bucket."""
        j = self._hash_function(k)
        for idx, tup in enumerate(self._table[j]):
            if k in tup:                      # Key exists in bucket
                del self._table[j][idx]       # Delete key-value pair
                self._n -= 1
                return
        raise KeyError('Invalid key!')        # Key not found in bucket

    def _hash_function(self, k):
        """Return hashed and compressed key."""
        return (3*k + 5) % self._cap

    def __iter__(self):
        """Return all buckets, even empty ones."""
        for bucket in self._table:
            yield [tup[1] for tup in bucket]  # Yield value of key-vaue pair


class SimpleLinearProbeHashTable(SimpleChainHashTable):
    """Solution to exercise R-10.10.

    What is the result of the previous exercise, assuming collisions are han-
    dled by linear probing?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    If a collision occurs, linear probing will will increment the index as
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

    _AVAIL = object()       # sentinal marks locations of previous deletions

    def __init__(self, cap=11):
        """Initialize a simple class with a subset of hash table methods."""
        super().__init__(cap)
        self._table = [None] * self._cap  # Override parent's _table variable
        self._start_idx = 0               # Track starting index during probing
        self._avail = SimpleLinearProbeHashTable._AVAIL

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or\
            self._table[j] is self._avail

    def _find_key(self, j, k):
        """Search for a matching key using linear probing.

        Return table index containing the key-value pair, or None if not found.
        """
        if j == self._start_idx:
            return None       # Search wrapped table, no key found (base case)
        if self._table[j] is None:
            return None             # Key not found in open bucket (base case)
        if self._table[j] is not self._avail and\
                self._table[j][0] == k:
            return j                # Key found, return index (base case)
        return self._find_key((j+1) % self._cap, k)

    def _find_slot(self, j):
        """Search for an available slot using linear probing.

        Return table index of the next available slot.
        """
        if self._is_available(j):
            return j          # Found available slot (base case)
        return self._find_slot((j+1) % self._cap)

    def __getitem__(self, k):
        """Return bucket located at index associated with key."""
        j = self._hash_function(k)
        if self._table[j] is None:
            raise KeyError('Invalid key!')   # Key not found in bucket
        if self._table[j] is not self._avail and\
                self._table[j][0] == k:
            return self._table[j][1]         # Key matches
        self._start_idx = j
        key_idx = self._find_key((j+1) % self._cap, k)  # Linear probing
        if key_idx is None:
            raise KeyError('Invalid key!')   # Key not found in table
        return self._table[key_idx][1]       # Key matches

    def __setitem__(self, k, v):
        """Add key-value pair to hash table.

        Overwrite the value of existing key.
        """
        j = self._hash_function(k)
        if self._table[j] is None:
            self._table[j] = (k, v)          # Key is new, write to table
            self._n += 1
            return
        if not self._is_available(j) and self._table[j][0] == k:
            self._table[j] = (k, v)          # Overwrite current value
            return
        self._start_idx = j
        next_j = (j+1) % self._cap
        key_idx = self._find_key(next_j, k)  # Check if key exists in table
        if key_idx:
            self._table[key_idx] = (k, v)    # Overwrite current value
            return
        if self._n == self._cap:             # If full table raise error, else:
            raise KeyError('Table is full!')
        avail_idx = self._find_slot(j)       # There must be an available slot
        self._table[avail_idx] = (k, v)      # Create new key-value pair
        self._n += 1

    def __delitem__(self, k):
        """Delete key-value pair if it exists in bucket."""
        j = self._hash_function(k)
        if self._table[j] is None:
            raise KeyError('Invalid key!')    # Key not found in bucket
        if not self._is_available(j):
            if self._table[j][0] == k:
                self._table[j] = self._avail
                self._n -= 1
                return
        if self._table[j] is self._avail or\
                self._table[j][0] != k:
            self._start_idx = j
            key_idx = self._find_key((j+1) % self._cap, k)  # Linear probing
        if key_idx is None:
            raise KeyError('Invalid key!')    # Key not found in bucket
        self._table[key_idx] = self._avail    # Key matches
        self._n -= 1

    def __iter__(self):
        """Return all buckets, even empty ones."""
        for idx, bucket in enumerate(self._table):
            if not self._is_available(idx):
                yield bucket[1]  # Yield value of key-vaue pair
            else:
                yield bucket


class SimpleQuadraticProbeHashTable(SimpleLinearProbeHashTable):
    """Solution to exercise R-10.11.

    Show the result of Exercise R-10.9, assuming collisions are handled by
    quadratic probing, up to the point where the method fails.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    If a collision occurs, quadratic probing will will increment the index as
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

    def _find_key(self, j, k):
        """Search for a matching key using quadratic probing.

        Return table index containing the key-value pair, or None if not found.
        """

        def recurse(j, k, i):
            next_idx = (j + i ** 2) % self._cap
            if next_idx == self._start_idx:
                return None  # Search wrapped table, no key found (base case)
            if self._table[next_idx] is None:
                return None  # Key not found in open bucket (base case)
            if self._table[next_idx] is not self._avail and\
                    self._table[next_idx][0] == k:
                return next_idx          # Key found, return index (base case)
            return recurse(j, k, i+1)

        return recurse((j-1) % self._cap, k, 1)

    def _find_slot(self, j):
        """Search for an available slot using quadratic probing.

        Return table index of the next available slot, or None if not found.
        """

        def recurse(j, i):
            next_idx = (j + i ** 2) % self._cap
            if next_idx == self._start_idx:
                return None  # Search wrapped table, no key found (base case)
            if self._is_available(next_idx):
                return next_idx          # Found available slot (base case)
            return recurse(j, i+1)

        self._start_idx = j
        return recurse(j, 1)


class SimpleSecondaryHashTable(SimpleLinearProbeHashTable):
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

    def _find_key(self, j, k):
        """Search for a matching key using secondary hashing.

        Return table index containing the key-value pair, or None if not found.
        """

        def recurse(j, k, i):
            next_idx = (j + i * h_prime) % self._cap
            if next_idx == self._start_idx:
                return None  # Search wrapped table, no key found (base case)
            if self._table[next_idx] is None:
                return None  # Key not found in open bucket (base case)
            if self._table[next_idx] is not self._avail and\
                    self._table[next_idx][0] == k:
                return next_idx          # Key found, return index (base case)
            return recurse(j, k, i+1)

        h_prime = 7 - (k % 7)
        return recurse((j-1) % self._cap, k, 1)

    def _find_slot(self, j, k):
        """Search for an available slot using secondary hashing.

        Return table index of the next available slot.
        """

        def recurse(j, i):
            next_idx = (j + i * h_prime) % self._cap
            if self._is_available(next_idx):
                return next_idx          # Found available slot (base case)
            return recurse(j, i+1)

        h_prime = 7 - (k % 7)
        self._start_idx = j
        return recurse(j, 1)

    def __setitem__(self, k, v):
        """Override parent class so that key is passed to _find_slot()."""
        j = self._hash_function(k)
        if self._table[j] is None:
            self._table[j] = (k, v)          # Key is new, write to table
            self._n += 1
            return
        if not self._is_available(j) and self._table[j][0] == k:
            self._table[j] = (k, v)          # Overwrite current value
            return
        self._start_idx = j
        next_j = (j+1) % self._cap
        key_idx = self._find_key(next_j, k)  # Check if key exists in table
        if key_idx:
            self._table[key_idx] = (k, v)    # Overwrite current value
            return
        if self._n == self._cap:             # If full table raise error, else:
            raise KeyError('Table is full!')
        avail_idx = self._find_slot(j, k)    # There must be an available slot
        self._table[avail_idx] = (k, v)      # Create new key-value pair
        self._n += 1


def worst_case_chaining():
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
    return True


class SimpleChainHashTableP14(SimpleChainHashTable):
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

    def __init__(self, cap=19):
        """Initialize a simple class with a subset of hash table methods."""
        super().__init__(cap)

    def _hash_function(self, k):
        """Return hashed and compressed key."""
        return (3*k) % 17


def not_suited():
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
    return True


def worst_case_asymp_running_time():
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
    return True
