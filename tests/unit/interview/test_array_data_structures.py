"""Test array-based classes used to solve robot path programming test.

###############################################################################
# test_array_data_structures.py
#
# Revision:     1.00
# Date:         7/22/2021
# Author:       Alex
#
# Purpose:      Unit test each individual component of the solution to the
#               robot programming exercise.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports
import pytest

# Local application/library specific imports
from interview.array_data_structures import Map, Queue


# %% Test Map class and nested _Item class
def test_item():
    """Test methods of nested _Item class."""
    item_a = Map._Item('a', 1)
    item_b = Map._Item('b', 2)
    # Test instance variables
    assert item_a._key == 'a'
    assert item_a._value == 1
    # Test comparisons
    assert item_a < item_b
    assert item_a != item_b
    assert item_b > item_a
    assert item_b >= item_a
    assert item_a <= item_b
    assert item_a == item_a


def test_map():
    """Test methods of Map class."""
    keys = 'abcdefghijklmnopqrstuvwxyz'
    a_map = Map()
    for val, key in enumerate(keys):
        a_map[key] = val                 # Test setting items
    assert len(a_map) == len(keys)       # Test length method
    for val, key in enumerate(keys):
        assert a_map[key] == val         # Test getting items
    for key, val in a_map:
        assert keys[val] == key          # Test iterating through keys
    for val, key in enumerate(keys):
        a_map[key] = val+1               # Test overwriting existing keys
    for val, key in enumerate(keys):
        assert a_map[key] == val+1       # Verify values are overwritten
    with pytest.raises(KeyError):
        print(a_map['abc'])              # Attempt to get nonexistent key
    with pytest.raises(KeyError):
        del a_map['abc']                 # Attempt to delete nonexistent key
    with pytest.raises(TypeError):
        print(a_map[{}])                 # Attempt to get unhashable key
    for key, val in list(a_map):
        del a_map[key]                   # Test deleting items
        with pytest.raises(KeyError):
            print(a_map[key])            # Verify item is deleted
    assert len(a_map) == 0               # Verify all items are deleted
    assert len(a_map._hash_table) == \
        a_map._default_capacity          # Verify hash table resized smaller
    for idx in range(0, len(keys)-3, 3):
        a_map[keys[idx:idx+3]] = idx     # Verify map works with longer keys
        assert a_map[keys[idx:idx+3]] == idx
    a_map[27] = 32
    a_map[3.234] = 'cow'
    assert a_map[27] == 32               # Verify map works with integer keys
    assert a_map[3.234] == 'cow'         # Verify map works with float keys
    assert a_map.get(5553) is None       # Test get() method w/o default value
    assert a_map.get(3442, 7) == 7       # Test get() method w/ default value


# %% Test Queue class
def test_queue():
    """Test methods of Queue class."""
    q = Queue()
    assert q.is_empty()
    assert len(q) == 0
    with pytest.raises(ValueError):
        q.first()                       # Should raise error on empty queue
    with pytest.raises(ValueError):
        q.last()                        # Should raise error on empty queue
    with pytest.raises(ValueError):
        q.dequeue()                     # Should raise error on empty queue
    n = 30
    for x in range(n):
        q.enqueue(x)
    assert q.first() == 0               # Test first()
    assert q.last() == n-1              # Test last()
    assert len(q) == n                  # Test enqueue()
    for x in range(n//2):
        assert x == q.dequeue()         # Test dequeue() FIFO order
    assert len(q) == n//2               # Elements still remain in queue
    for x in range(n, 2*n):
        q.enqueue(x)                    # Add more elements to queue
    assert len(q) == n + n//2
    for x in range(len(q)):
        assert x + n//2 == q.dequeue()  # Test FIFO order of queue
    assert q.is_empty()
