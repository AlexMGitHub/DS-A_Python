"""Test linked-list classes used to solve robot path programming test.

###############################################################################
# test_linked_list_data_structures.py
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
from interview.linked_list_data_structures import DoublyLinkedList
from interview.linked_list_data_structures import PositionalList
from interview.array_data_structures import Map


# %% Test DoublyLinkedList, PositionalList, and nested _Position classes
def test_doublylinkedlist():
    """Test methods of DoublyLinkedList class."""
    dll = DoublyLinkedList()
    assert dll.is_empty()
    assert len(dll) == 0
    node = dll._insert_node(0, dll._header, dll._trailer)
    assert not dll.is_empty()
    assert len(dll) == 1
    n = 10
    for x in range(1, n):
        node = dll._insert_node(x, node, dll._trailer)  # Add elements to list
    assert len(dll) == n
    for x in range(n):
        element = dll._delete_node(dll._header._next)   # Delete all nodes
        assert element == x
    assert dll.is_empty()
    assert len(dll) == 0


def test_position():
    """Test methods of nested _Position class."""
    pos_list = PositionalList()
    pos_a = pos_list.add_first('a')
    pos_b = pos_list.add_first('b')
    # Test methods
    assert pos_a.element() == 'a'
    assert pos_b.element() == 'b'
    # Test comparisons
    assert pos_a == pos_a
    assert pos_a != pos_b
    # Test hashing Position objects
    pos_map = Map()
    pos_map[pos_a] = 1
    pos_map[pos_b] = 2
    assert pos_map[pos_a] == 1
    assert pos_map[pos_b] == 2


def test_error_catching():
    """Test error catching of various methods of PositionalList class."""
    pos_list = PositionalList()
    assert pos_list.is_empty()
    assert len(pos_list) == 0
    with pytest.raises(ValueError):
        pos_list.first()                      # List empty
    with pytest.raises(ValueError):
        pos_list.last()                       # List empty
    only_pos = pos_list.add_first('abc')
    assert pos_list.first().element() == pos_list.last().element() == 'abc'
    assert pos_list.before(only_pos) is None  # No prev position in list
    assert pos_list.after(only_pos) is None   # No next position in list


def test_invalid_positions():
    """Test invalid nodes and positions of PositionalList class."""
    pos_list = PositionalList()
    only_pos = pos_list.add_first('abc')
    assert pos_list._wrap_node(pos_list._header) is None   # Sentinel node
    assert pos_list._wrap_node(pos_list._trailer) is None  # Sentinel node
    with pytest.raises(TypeError):
        pos_list._validate_position(1)       # Not a valid Position object
    pos_list2 = PositionalList()
    wrong_list = pos_list2.add_first('abc')  # Position from another list
    with pytest.raises(ValueError):
        pos_list._validate_position(wrong_list)  # Belongs to another list
    deleted_node = only_pos._node  # Create reference to node to be deleted
    pos_list.delete(only_pos)      # Delete position containing node
    invalid_pos = PositionalList._Position(deleted_node, pos_list)
    with pytest.raises(ValueError):
        pos_list._validate_position(invalid_pos)  # References invalid node


def test_public_methods():
    """Test public methods of PositionalList class."""
    pos_list = PositionalList()
    assert pos_list.is_empty()
    assert len(pos_list) == 0
    n = 10
    for x in range(n//2):
        pos_list.add_first(x)                       # Test add_first()
    for idx, element in enumerate(pos_list):
        assert element == n//2-1 - idx              # Test __iter__()
    for x in range(n//2, n):
        pos_list.add_last(x)                        # Test add_last()
    first_pos = pos_list.first()
    last_pos = pos_list.last()
    second_pos = pos_list.after(first_pos)
    second_last_pos = pos_list.before(last_pos)
    assert first_pos.element() == n//2-1            # Test first()
    assert last_pos.element() == n-1                # Test last()
    assert second_pos.element() == n//2-2           # Test after()
    assert second_last_pos.element() == n-2         # Test before()
    old_element = pos_list.replace(pos_list.first(), 'abc')
    assert old_element == n//2-1
    assert pos_list.first().element() == 'abc'      # Test delete()
    after_pos = pos_list.add_after(pos_list.first(), 'cat')
    pos_list.add_before(after_pos, 'dog')
    expected_order = ('abc', 'dog', 'cat')
    for x, y in zip(expected_order, pos_list):
        assert x == y  # Test add_before() and add_after()
