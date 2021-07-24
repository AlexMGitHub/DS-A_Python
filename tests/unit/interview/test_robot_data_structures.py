"""Test classes used to solve robot path programming test.

###############################################################################
# test_robot_data_structures.py
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
import numpy as np

# Local application/library specific imports
from interview.robot_data_structures import Map
from interview.robot_data_structures import DoublyLinkedList
from interview.robot_data_structures import PositionalList
from interview.robot_data_structures import Graph


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


# %% Test Graph class and nested Vertex and Edge classes.
def test_vertex():
    """Test methods of the nested _Vertex class."""
    graph = Graph()
    vert_a = graph.insert_vertex('a')
    vert_b = graph.insert_vertex('b')
    # Test methods
    assert vert_a.element() == 'a'
    assert vert_b.element() == 'b'
    # Test hashing Vertex objects
    vert_map = Map()
    vert_map[vert_a] = 1
    vert_map[vert_b] = 2
    assert vert_map[vert_a] == 1
    assert vert_map[vert_b] == 2


def test_edge():
    """Test methods of the nested _Edge class."""
    graph = Graph()
    vert_a = graph.insert_vertex('a')
    vert_b = graph.insert_vertex('b')
    edge = graph.insert_edge(vert_a, vert_b, 5)
    # Test methods
    assert edge._origin == vert_a
    assert edge._destination == vert_b
    assert edge.element() == 5
    assert edge.endpoints() == (vert_a, vert_b)
    assert edge.opposite(vert_a) == vert_b
    assert edge.opposite(vert_b) == vert_a
    # Test hashing Vertex objects
    edge2 = graph.insert_edge(vert_b, vert_a, 7)
    edge_map = Map()
    edge_map[edge] = 1
    edge_map[edge2] = 2
    assert edge_map[edge] == 1
    assert edge_map[edge2] == 2


def test_graph():
    """Test methods of the Graph class for directed and undirected graphs."""
    rng = np.random.default_rng(55)
    graph = Graph()
    dgraph = Graph(directed=True)
    n = 30      # Number of vertices n
    m = 60      # Number of edges m
    gvert_list = []
    dgvert_list = []
    for x in range(n):
        gvert_list.append(graph.insert_vertex(x))
        dgvert_list.append(dgraph.insert_vertex(x))
    assert graph.vertex_count() == dgraph.vertex_count() == n  # Vertex count
    assert len(graph.vertices) == len(dgraph.vertices) == n  # Vertex iteration
    for x in range(m):
        g_samples = rng.choice(gvert_list, size=2)  # Randomly select 2 verts
        dg_samples = rng.choice(dgvert_list, size=2)
        graph.insert_edge(g_samples[0], g_samples[1], x)  # Insert edge
        dgraph.insert_edge(dg_samples[0], dg_samples[1], x)
    assert graph.edge_count() == dgraph.edge_count() == m  # Edge count
    assert len(graph.edges) == len(dgraph.edges) == m      # Sets of edges


if __name__ == '__main__':
    test_vertex()
