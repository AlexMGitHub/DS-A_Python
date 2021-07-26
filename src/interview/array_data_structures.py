"""Array-based data structure classes.

###############################################################################
# array_data_structures.py
#
# Revision:     1.00
# Date:         7/22/2021
# Author:       Alex
#
# Purpose:      Implementations of various data structures used to solve the
#               robot programming exercise.
#
# Contents:
#
#   Map: Implements a map using a dynamic hash table with separate chaining.
#
#   Queue: Implementation of a queue using a circular dynamic array.
#
###############################################################################
"""

# %% Imports
# Standard system imports
from collections.abc import Hashable

# Related third party imports
import numpy as np

# Local application/library specific imports


# %% Classes
class Map:
    """Implements a map using a dynamic hash table with separate chaining."""

    class _Item:
        """Class to contain (key, value) pairs stored in Map."""

        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            """Store key and value."""
            self._key = key
            self._value = value

        def __eq__(self, other):
            """Return True if two keys are equal."""
            return self._key == other._key

        def __ne__(self, other):
            """Return True if two keys are not equal."""
            return not self == other

        def __lt__(self, other):
            """Return True if key less than other key."""
            return self._key < other._key

        def __gt__(self, other):
            """Return True if key greater than other key."""
            return self._key > other._key

        def __ge__(self, other):
            """Return True if key greater than or equal to other key."""
            return self._key >= other._key

        def __le__(self, other):
            """Return True if key less than or equal to other key."""
            return self._key <= other._key

    def __init__(self, capacity=11, prime=109345121):
        """Initialize an empty hash table of specified capacity.

        The default capacity and prime number used for MAD compression are
        optional.  Randomly calculates the scale and shift values for MAD
        compression.
        """
        self._hash_table = [[] for _ in range(capacity)]
        self._n = 0  # Current length of hash table
        self._default_capacity = capacity
        self._prime = prime  # Large prime used for MAD compression
        self._scale = np.random.randint(1, self._prime)
        self._shift = np.random.randint(0, self._prime)

    def __getitem__(self, key):
        """Return value associated with requested key.

        Raise key error if not found.
        """
        idx = self._hash_code(key)
        for item in self._hash_table[idx]:
            if key == item._key:
                return item._value
        raise KeyError('Key not found!')

    def get(self, key, default=None):
        """Attempt to get key; if it does not exist return default value."""
        try:
            return self[key]
        except KeyError:
            return default

    def __setitem__(self, key, value):
        """If key exists in hash table overwrite value, otherwise add item."""
        idx = self._hash_code(key)
        for item in self._hash_table[idx]:
            if key == item._key:
                item._value = value  # Key exists, overwrite its value
                return
        self._n += 1  # New key, add new item
        self._hash_table[idx].append(self._Item(key, value))
        if self._n > len(self._hash_table) // 2:  # Double capacity of table
            self._resize_table(2 * len(self._hash_table) - 1)

    def __delitem__(self, key):
        """Delete item associated with key.

        Raise key error if not found.
        """
        idx = self._hash_code(key)
        for subidx, item in enumerate(self._hash_table[idx]):
            if key == item._key:
                self._n -= 1  # Delete existing key
                del self._hash_table[idx][subidx]
                if self._n < len(self._hash_table) // 4 and \
                        len(self._hash_table) > self._default_capacity:
                    self._resize_table(len(self._hash_table) // 2 + 1)  # Halve
                return
        raise KeyError('Key not found!')

    def __len__(self):
        """Return length of hash table."""
        return self._n

    def __iter__(self):
        """Iterate through hash table and return (key, value) tuples."""
        for bucket in self._hash_table:
            for item in bucket:
                yield (item._key, item._value)

    def _hash_code(self, key):
        """Return compressed hash code calculated using 5-bit cyclic shift.

        Raises ValueError if key is not hashable.
        """
        if not isinstance(key, Hashable):
            raise TypeError('Invalid key!')
        if isinstance(key, int):
            bin_key = bin(key)          # For integer keys
        elif isinstance(key, str):
            bin_key = key               # For string keys
        else:
            bin_key = bin(hash(key))    # Floats and other hashable types
        mask = (1 << 32) - 1  # All 1s in binary, limit hash code to 32 bits
        hash_code = 0
        for character in bin_key:
            hash_code = (hash_code << 5 & mask) | (hash_code >> 27)
            hash_code += ord(character)  # Single-character keys not shifted
        return self._compression_function(hash_code)

    def _compression_function(self, hash_code):
        """Compresses the hash code using the MAD method."""
        p = self._prime
        a = self._scale
        b = self._shift
        N = len(self._hash_table)
        return ((a * hash_code + b) % p) % N

    def _resize_table(self, capacity):
        """Transfer key-value pairs to resized hash table."""
        old_table = list(self)  # List of (key, value) tuples
        self._hash_table = self._make_table(capacity)
        self._n = 0             # Reset length of hash table
        for key, value in old_table:
            self[key] = value   # Add key-value pairs to resized hash table

    def _make_table(self, capacity):
        """Return a list of empty lists, length equal to requested capacity."""
        return [[] for _ in range(capacity)]


class Queue:
    """Implementation of a queue using a circular dynamic array."""

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Initialize empty array for queue."""
        self._size = 0
        self._array = [None] * Queue.DEFAULT_CAPACITY
        self._front = 0     # Index of first element in array

    @property
    def _N(self):
        """Return length of dynamic array used to implement queue."""
        return len(self._array)

    def enqueue(self, element):
        """Add element to the back of the queue."""
        index = (self._front + self._size) % self._N
        self._array[index] = element
        self._size += 1
        if self._size == self._N:
            self._resize_array(self._N * 2)  # Double size of array

    def dequeue(self):
        """Remove and return element from the front of the queue.

        Raise ValueError if queue is empty.
        """
        if self.is_empty():
            raise ValueError('Queue is empty!')
        element = self._array[self._front]
        self._array[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % self._N  # Move front right
        if self._size == self._N // 4 and self._N > Queue.DEFAULT_CAPACITY:
            self._resize_array(self._N // 2)  # Halve size of array
        return element

    def first(self):
        """Return (but do not remove) element at the front of the queue.

        Raise ValueError if queue is empty.
        """
        if self.is_empty():
            raise ValueError('Queue is empty!')
        return self._array[self._front]

    def last(self):
        """Return (but do not remove) element at the back of the queue.

        Raise ValueError if queue is empty.
        """
        if self.is_empty():
            raise ValueError('Queue is empty!')
        return self._array[(self._front + self._size - 1) % self._N]

    def __len__(self):
        """Return length of queue."""
        return self._size

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0

    def _resize_array(self, capacity):
        """Copy element of queue to new array of specified capacity."""
        old_N = self._N
        old_array = self._array
        self._array = [None] * capacity
        for index in range(self._size):
            self._array[index] = old_array[(self._front + index) % old_N]
        self._front = 0  # Copied queue starts at index 0
