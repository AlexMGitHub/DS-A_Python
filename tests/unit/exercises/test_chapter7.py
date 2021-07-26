#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 7 exercises.

###############################################################################
# test_chapter7.py
#
# Revision:     1.00
# Date:         7/2/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 7 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports
from copy import deepcopy

# Related third party imports
import pytest

# Local application/library specific imports
import dsa.chapter7_exercises as chap7
from textbook_src.ch07.favorites_list_mtf import FavoritesListMTF
from textbook_src.ch07.positional_list import PositionalList


# %% Reinforcement Exercises
def test_sll():
    """Test all methods of the SinglyLinkedList class."""
    singly = chap7.SinglyLinkedList()
    # Test Empty exception conditions
    with pytest.raises(chap7.Empty):
        singly.head()
    with pytest.raises(chap7.Empty):
        singly.tail()
    with pytest.raises(chap7.Empty):
        singly.pop()
    with pytest.raises(chap7.Empty):
        singly.traverse(1)
    with pytest.raises(chap7.Empty):
        singly.get_node(1)
    # Test node operations
    for x in range(20):
        singly.add_last(x)
    singly.head()
    singly.tail()
    singly.pop()
    len(singly)
    singly.add_first(0)
    singly.traverse(4)
    singly.get_node(6)
    # Test IndexError exception conditions
    with pytest.raises(IndexError):
        singly.traverse(-1)
    with pytest.raises(IndexError):
        singly.get_node(40)
    # Test add_first on empty list
    singly2 = chap7.SinglyLinkedList()
    singly2.add_first(1)


def test_dll():
    """Test all methods of the DoublyLinkedList class."""
    doubly = chap7.DoublyLinkedList()
    # Test Empty exception conditions
    with pytest.raises(chap7.Empty):
        doubly.head()
    with pytest.raises(chap7.Empty):
        doubly.tail()
    with pytest.raises(chap7.Empty):
        doubly.delete_first()
    with pytest.raises(chap7.Empty):
        doubly.delete_last()
    with pytest.raises(chap7.Empty):
        doubly.forward_traverse(1)
    with pytest.raises(chap7.Empty):
        doubly.get_node(1)
    # Test node operations
    for x in range(20):
        doubly.add_last(x)
    doubly.head()
    doubly.tail()
    doubly.delete_last()
    doubly.delete_first()
    len(doubly)
    doubly.add_first(0)
    doubly.forward_traverse(4)
    doubly.get_node(6)
    # Test IndexError exception conditions
    with pytest.raises(IndexError):
        doubly.forward_traverse(-1)
    with pytest.raises(IndexError):
        doubly.get_node(40)


def test_second_to_last():
    """Solution to exercise R-7.1.

    Give an algorithm for finding the second-to-last node in a singly linked
    list in which the last node is indicated by a next reference of None.
    """
    # Instantiate a singly linked list and add n elements to it
    singly = chap7.SinglyLinkedList()
    n = 10
    for x in range(1, n+1):
        singly.add_last(x)
    # Return the second-to-last node in the linked list
    second_to_last = singly.traverse(len(singly)-2)
    assert second_to_last == n-1
    # Check edge cases
    assert singly.traverse(len(singly)-1) == n  # Last item in list
    assert singly.traverse(0) == 1              # First item in list
    with pytest.raises(IndexError):
        singly.traverse(len(singly))            # Max index is n-1
    with pytest.raises(IndexError):
        singly.traverse(-1)                     # Min index is 0


@pytest.mark.parametrize('method', [chap7.concat_sll1, chap7.concat_sll2])
def test_concat_sll(method):
    """Solution to exercise R-7.2.

    Describe a good algorithm for concatenating two singly linked lists L and
    M, given only references to the first node of each list, into a single list
    L' that contains all the nodes of L followed by all the nodes of M.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Assumptions:
      1. We are allowed to modify/break L and M
      2. L_prime should point to same nodes as L and M; not create new nodes

    If assumption 1 is not allowed, assumption 2 will have to be invalidated.
    The tail node of L must point to the head node of M, which can't be done
    without either creating new nodes or modifying existing nodes.

    I've written solutions for both cases:
      1. Method 1: Traverse through nodes and connect L._tail to M._head
      2. Method 2: Traverse through L and add new nodes to L_prime with the
         values of L's elements; repeat with M
    """
    # Instantiate SLLs and add n/2 elements to each
    L = chap7.SinglyLinkedList()
    M = chap7.SinglyLinkedList()
    n = 20
    for x in range(n):
        if x < n // 2:
            L.add_last(x)
        else:
            M.add_last(x)
    # Make copies of lists for later tests
    L2 = deepcopy(L)
    M2 = deepcopy(M)
    # Concatenate list, and traverse result to ensure values are correct
    L_prime = method(L._head, M._head)
    for x in range(n):
        assert L_prime.traverse(x) == x
    assert len(L_prime) == len(L) + len(M)
    # Test concatenating with empty lists
    m_empty = method(L2._head, None)
    for x in range(len(m_empty)):
        assert m_empty.traverse(x) == x
    l_empty = method(None, M2._head)
    for x in range(len(l_empty)):
        assert l_empty.traverse(x) == x + n // 2
    null = method(None, None)
    assert null._head is null._tail is None
    assert len(null) == 0


def test_recursive_node_count():
    """Solution to exercise R-7.3.

    Describe a recursive algorithm that counts the number of nodes in a singly
    linked list.
    """
    # Instantiate SLL and add nodes
    singly = chap7.SinglyLinkedList()
    n = 20
    for x in range(n):
        singly.add_last(x)
    assert chap7.recursive_node_count(singly) == n
    # Make sure an empty list is counted properly
    empty = chap7.SinglyLinkedList()
    assert chap7.recursive_node_count(empty) == 0


def test_node_swap():
    """Solution to exercise R-7.4.

    Describe in detail how to swap two nodes x and y (and not just their con-
    tents) in a singly linked list L given references only to x and y. Repeat
    this exercise for the case when L is a doubly linked list. Which algorithm
    takes more time?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The singly linked list algorithm will take more time in general, because it
    must first traverse the list to find the previous nodes of both x and y.
    Worst-case this will take O(n) time, as the entire list may have to be
    traversed to find both nodes.

    The nodes of the doubly linked list already contain references to both of
    their neighboring nodes, and so the only work required is a swap of
    the references.  This is O(1) time as it does not depend on the length of
    the list or the positions of the nodes within the list.
    """
    # Instantiate SLL and DLL and add nodes
    singly = chap7.SinglyLinkedList()
    doubly = chap7.DoublyLinkedList()
    n = 20
    for x in range(n):
        singly.add_last(x)
        doubly.add_last(x)
    # Test singly linked list
    # Swap node after header (index 1) with node before tail (index n-2)
    node1 = singly.get_node(1)
    node2 = singly.get_node(n-2)
    chap7.node_swap(singly, node1, node2)   # Swap nodes in singly linked list
    assert singly.traverse(1) == n-2        # Verify nodes are swapped
    assert singly.traverse(n-2) == 1
    assert singly.traverse(0) == 0          # Verify head is still same value
    assert singly.traverse(n-1) == n-1      # Verify tail is still same value
    for x in range(2, n-2):
        assert singly.traverse(x) == x  # Verify all other nodes are the same
    # Test doubly linked list
    # Swap node after header (index 1) with node before tail (index n-2)
    node1 = doubly.get_node(1)
    node2 = doubly.get_node(n-2)
    chap7.node_swap(doubly, node1, node2)   # Swap nodes in doubly linked list
    assert doubly.forward_traverse(1) == n-2  # Verify nodes are swapped
    assert doubly.forward_traverse(n-2) == 1
    assert doubly.forward_traverse(0) == 0    # Verify head is still same value
    assert doubly.forward_traverse(n-1) == n-1  # Verify tail is still same
    for x in range(2, n-2):
        assert doubly.forward_traverse(x) == x  # Verify all other nodes same


def test_circular_count():
    """Solution to exercise R-7.5.

    Implement a function that counts the number of nodes in a circularly
    linked list.
    """
    circ = chap7.CircularQueue()
    assert chap7.circular_count(circ) == 0  # Verify empty list returns 0 count
    n = 20
    for x in range(n):
        circ.enqueue(x)
    assert chap7.circular_count(circ) == n


def test_node_from_same_list():
    """Solution to exercise R-7.6.

    Suppose that x and y are references to nodes of circularly linked lists,
    although not necessarily the same list. Describe a fast algorithm for
    telling if x and y belong to the same list.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    My solution is to simply override the internal _Node class of the circular
    list to include a reference to the list that contains the node.  This is
    the same approach used by the Position() class in a positional list.
    """
    circ1 = chap7.CircularListIdentify()
    circ2 = chap7.CircularListIdentify()
    n = 10
    for x in range(n):
        circ1.enqueue(x)
        circ2.enqueue(x)
    # Test that nodes from two different lists can be distinguished
    assert circ1._tail._list is not circ2._tail._list
    # Test that different nodes can be identified as from the same list
    assert circ1._tail._next._list is circ1._tail._list
    assert circ2._tail._next._list is circ2._tail._list


def test_rotate_linked_queue():
    """Solution to exercise R-7.7.

    Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
    has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty
    queue. Implement such a method for the LinkedQueue class of Section
    7.1.2 without the creation of any new nodes.
    """
    linked_queue = chap7.RotateLinkedQueue()
    n = 10
    for x in range(n):
        linked_queue.enqueue(x)
    assert linked_queue.first() == 0
    assert linked_queue._tail._element == n-1
    # Test the nodes are properly rotated
    linked_queue.rotate()
    for x in range(n):
        element = linked_queue.dequeue()
        if x == 0:
            assert element == n-1       # First element should be last value
        elif x == n-1:
            assert element == 0         # Last element should be first value
        else:
            assert element == x         # Other elements should be unchanged


def test_find_middle_node():
    """Solution to exercise R-7.8.

    Describe a nonrecursive method for finding, by link hopping, the middle
    node of a doubly linked list with header and trailer sentinels. In the case
    of an even number of nodes, report the node slightly left of center as the
    “middle.” (Note: This method must only use link hopping; it cannot use a
    counter.) What is the running time of this method?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    My solution is to use the doubly linked list's _size parameter to link-hop
    to the middle node of the list.  The running time is O(n), as there will be
    n/2 link hops required to find the middle node.
    """
    doubly_even = chap7.DoublyLinkedList()
    doubly_odd = chap7.DoublyLinkedList()
    doubly_empty = chap7.DoublyLinkedList()
    n = 20
    for x in range(20):
        doubly_even.add_last(x)
        doubly_odd.add_last(x)
    doubly_odd.add_last(n)  # Add one more element so total is an odd number
    even_middle_node = chap7.find_middle_node(doubly_even)
    odd_middle_node = chap7.find_middle_node(doubly_odd)
    empty_middle_node = chap7.find_middle_node(doubly_empty)
    assert even_middle_node._element == (n-1) // 2
    assert odd_middle_node._element == (n) // 2
    assert empty_middle_node is None


def test_concat_dll():
    """Solution to exercise R-7.9.

    Give a fast algorithm for concatenating two doubly linked lists L and M,
    with header and trailer sentinel nodes, into a single list L'.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I assume for this exercise that L and M can be modified, and that L' should
    refer to the original nodes (not create new ones).
    """
    # Instantiate DLLs and add n/2 elements to each
    L = chap7.DoublyLinkedList()
    M = chap7.DoublyLinkedList()
    n = 20
    for x in range(n):
        if x < n // 2:
            L.add_last(x)
        else:
            M.add_last(x)
    # Concatenate list, and traverse result to ensure values are correct
    L_prime = chap7.concat_dll(L, M)
    for x in range(n):
        assert L_prime.forward_traverse(x) == x
    assert len(L_prime) == len(L) + len(M)


def test_positional_adt():
    """Solution to exercise R-7.10.

    There seems to be some redundancy in the repertoire of the positional
    list ADT, as the operation L.add_first(e) could be enacted by the alter-
    native L.add_before(L.first( ), e). Likewise, L.add_last(e) might be per-
    formed as L.add_after(L.last( ), e). Explain why the methods add_first
    and add_last are necessary.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The methods add_first() and add_last() accept elements as arguments, while
    add_before() and add_after() accept a position and an element as arguments.
    It wouldn't be possible to add a new element to an empty positional list
    using add_before() or add_after(), because there are no existing positions
    to pass as arguments to these methods.
    """
    assert chap7.positional_adt()


def test_pl_max():
    """Solution to exercise R-7.11.

    Implement a function, with calling syntax max(L), that returns the max-
    imum element from a PositionalList instance L containing comparable
    elements.
    """
    pos_list = PositionalList()
    n = 20
    for x in range(n):
        pos_list.add_last(x)
    assert chap7.pl_max(pos_list) == n-1
    pos_list.add_first(2*n)
    assert chap7.pl_max(pos_list) == 2*n


def test_pl_max_method():
    """Solution to exercise R-7.12.

    Redo the previously problem with max as a method of the PositionalList
    class, so that calling syntax L.max( ) is supported.
    """
    pos_list = chap7.PositionalListMax()  # Subclass of PositionalList w/ max()
    n = 20
    for x in range(n):
        pos_list.add_last(x)
    assert pos_list.max() == n-1
    pos_list.add_first(2*n)
    assert pos_list.max() == 2*n


def test_pl_find_method():
    """Solution to exercise R-7.13.

    Update the PositionalList class to support an additional method find(e),
    which returns the position of the (first occurrence of ) element e in the
    list (or None if not found).
    """
    pos_list = chap7.PositionalListFind()
    n = 20
    for x in range(n):
        pos_list.add_last(x)
    pos_e = pos_list.find(n // 2)
    assert pos_e.element() == n // 2
    pos_none = pos_list.find(2*n)
    assert pos_none is None


def test_pl_recursive_find_method():
    """Solution to exercise R-7.14.

    Repeat the previous process using recursion. Your method should not
    contain any loops. How much space does your method use in addition to
    the space used for L?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Each recursive function call is O(1) in terms of memory usage, as only the
    function's memory overhead and a pointer to the list position are needed.
    Worst-case the method will have to run though all n positions in the list,
    and so this method is O(n) in terms of memory usage.
    """
    pos_list = chap7.PositionalListRecursiveFind()
    n = 20
    for x in range(n):
        pos_list.add_last(x)
    pos_e = pos_list.find(n // 2)
    assert pos_e.element() == n // 2
    pos_none = pos_list.find(2*n)
    assert pos_none is None


def test_pl_reverse_method():
    """Solution to exercise R-7.15.

    Provide support for a reversed method of the PositionalList class that
    is similar to the given iter , but that iterates the elements in reversed
    order.
    """
    pos_list = chap7.PositionalListReverse()
    n = 20
    for x in range(n):
        pos_list.add_last(x)
    for element, expected in zip(range(n-1, -1, -1), pos_list.reverse()):
        assert element == expected


def test_mtf_order():
    """Solution to exercise R-7.18.

    Given the set of element {a, b, c, d, e, f } stored in a list, show the
    final state of the list, assuming we use the move-to-front heuristic and
    access the elements according to the following sequence:
    (a, b, c, d, e, f , a, c, f , b, d, e).

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The move-to-front heuristic moves the last accessed item to the front of
    the list.  The items will be reordered according to the last 6 unique items
    accessed (in reverse order).
    """
    mtf = FavoritesListMTF()
    elements = ['a', 'b', 'c', 'd', 'e', 'f']
    for element in elements:
        mtf.access(element)  # Populate elements
    access_order = ('a', 'b', 'c', 'd', 'e', 'f', 'a', 'c', 'f', 'b', 'd', 'e')
    for element in access_order:
        mtf.access(element)
    expected_order = chap7.mtf_order()
    for item, expected in zip(mtf._data, expected_order):
        assert item._value == expected


def test_reverse_mtf():
    """Solution to exercise R-7.20.

    Let L be a list of n items maintained according to the move-to-front
    heuristic. Describe a series of O(n) accesses that will reverse L.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Access each member of the list in the reverse of the current order.
    This is an O(n) method that will reverse the order of the list.
    """
    mtf = FavoritesListMTF()
    n = 20
    for x in range(n):  # Populate list
        mtf.access(x)
    current_order = [item._value for item in mtf._data]
    # Verify order of populated list
    for element, expected in zip(current_order, range(n-1, -1, -1)):
        assert element == expected
    chap7.reverse_mtf(mtf, n)
    # Verify order has been reversed
    reverse_order = [item._value for item in mtf._data]
    for element, expected in zip(reverse_order, range(n)):
        assert element == expected
