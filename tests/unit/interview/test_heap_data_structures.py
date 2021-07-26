"""Test heap-based classes used to solve robot path programming test.

###############################################################################
# test_heap_data_structures.py
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
from interview.heap_data_structures import Heap, AdaptablePriorityQueue


# %% Test BinaryTree, Heap, and AdaptablePriorityQueue classes.
def test_node():
    """Test methods of nested _Node class defined in the BinaryTree class."""
    node_a = Heap._Node('a', None, None)
    node_b = Heap._Node('b', None, None)
    # Test methods
    assert node_a.element() == 'a'
    assert node_b.element() == 'b'
    # Test comparisons
    assert node_a == node_a
    assert node_a != node_b
    assert node_a < node_b
    assert node_a <= node_b
    assert node_b > node_a
    assert node_b >= node_a


def test_binary_tree():
    """Test the methods of the BinaryTree class inherited by the Heap class."""
    heap = Heap()
    n = 30
    for x in range(n):
        heap.insert_element(x)
    root = heap.root()                              # Test root()
    assert heap.is_root(root)                       # Test is_root()
    assert root.element() == 0                      # 0 should be at root
    assert len(list(heap.children(root))) == 2      # Root has two children
    assert heap.parent(root) is None                # Root has no parent node
    left = heap.left(root)
    right = heap.right(root)
    assert left.element() == 1          # Per CBT prop 1 should be left child
    assert right.element() == 2         # Value of 2 should be right child
    assert heap.sibling(left) == right  # Test sibling()
    assert heap.sibling(right) == left
    assert not heap.is_leaf(left)       # Left is internal node, not leaf
    for x, element in zip(heap, range(n)):
        assert x == element             # Test breadth-first search and iter()
    nodes = list(heap.nodes())
    assert len(nodes) == n              # Test nodes()
    last = nodes[-1]
    assert not heap.is_root(last)       # Last node in tree is not root
    assert heap.is_leaf(last)           # Last node in tree is leaf
    with pytest.raises(TypeError):
        heap.left('cat')                # Not a Node object
    wrong_heap = heap._Node(None, 0, None)
    with pytest.raises(ValueError):
        heap.right(wrong_heap)          # Node is not contained in heap
    invalid_node = heap._Node('abc', n, heap)
    with pytest.raises(ValueError):
        heap.sibling(invalid_node)      # Node's index is too large


def test_heap():
    """Test methods of the Heap class."""
    heap = Heap()
    n = 30
    for x in range(n-1, -1, -1):
        heap.insert_element(x)              # Insert elements in reverse order
    root = heap.root()
    assert heap.sibling(root) is None       # Root has no sibling
    last = heap.last_node()                 # Bottom-right most position
    assert heap.is_leaf(last)               # Last position is a leaf
    assert heap.sibling(last) is None       # Only child
    nodes = list(heap.nodes())
    middle = nodes[n//2]                    # Middle position in heap
    heap.update_node(middle, -1)
    assert heap.is_root(middle)             # Should up-heap bubble to root
    assert len(heap) == n                   # No change to number of positions
    down = heap.root()                      # Root is currently value of -1
    heap.update_node(down, n)               # Down-heap bubble root value n
    assert heap.is_leaf(down)               # Should down-bubble to bottom
    for x in range(n-1):
        assert heap.remove_min() == x       # Delete roots, which should be
        assert len(heap) == n-1-x           # returned in nondecreasing order
    assert heap.remove_min() == n           # Last element should be n
    assert len(heap) == 0                   # "down" node was updated to n


def test_heap_rng():
    """Test Heap class using randomly generated integers."""
    rng = np.random.default_rng(103)            # Seeded random generator
    n = 100
    rints = rng.integers(low=0, high=1000, size=n)
    heap = Heap()
    node_list = []
    for x in rints:
        node_list.append(heap.insert_element(x))
    rints2 = rng.integers(low=0, high=1000, size=n)
    for idx, node in enumerate(node_list):
        heap.update_node(node, rints2[idx])     # Update nodes w/ new randints
    unsorted_list = []
    for _ in range(len(rints)):
        unsorted_list.append(heap.remove_min())
    sorted_list = sorted(unsorted_list)         # Use Python's sort function
    assert sorted_list == unsorted_list         # Ensure heap sorted elements


def test_item():
    """Test methods of nested Item class of AdaptablePriorityQueue."""
    item_a = AdaptablePriorityQueue._Item('a', 1)
    item_b = AdaptablePriorityQueue._Item('b', 2)
    # Test instance variables
    assert item_a.key() == 'a'
    assert item_a.value() == 1
    # Test comparisons
    assert item_a < item_b
    assert item_a != item_b
    assert item_b > item_a
    assert item_b >= item_a
    assert item_a <= item_b
    assert item_a == item_a


def test_adaptable_priority_queue():
    """Test methods of the AdaptablePriorityQueue class."""
    q = AdaptablePriorityQueue()
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
        q.enqueue(x, x)                 # Add elements to queue
    assert len(q) == n                  # Test enqueue()
    assert q.first() == 0               # Test first()
    assert q.last() == n-1
    for x in range(n//2):
        _, value = q.dequeue()
        assert x == value               # Test dequeue() in order of priority
    assert len(q) == n//2               # Elements still remain in queue
    for x in range(n//2):
        q.enqueue(x, x)                 # Add back in dequeued elements
    for x in range(n, 2*n):
        q.enqueue(x, x)                 # Add more elements to queue
    assert len(q) == 2*n
    for x in range(len(q)):
        _, value = q.dequeue()
        assert x == value               # Test dequeue() in order of priority
    assert q.is_empty()


def test_adp_rng():
    """Test AdaptablePriorityQueue class using randomly generated integers."""
    rng = np.random.default_rng(217)            # Seeded random generator
    n = 100
    rints = rng.integers(low=0, high=1000, size=n)
    q = AdaptablePriorityQueue()
    node_list = []
    for x in rints:
        node_list.append(q.enqueue(x, x))
    rints2 = rng.integers(low=0, high=1000, size=n)
    for idx, node in enumerate(node_list):
        key, value = rints2[idx], rints2[idx]
        q.update(node, key, value)              # Update nodes w/ new randints
    unsorted_list = []
    for _ in range(n):
        unsorted_list.append(q.dequeue()[1])    # Insert values into list
    sorted_list = sorted(unsorted_list)         # Use Python's sort function
    assert sorted_list == unsorted_list         # Ensure heap sorted elements
