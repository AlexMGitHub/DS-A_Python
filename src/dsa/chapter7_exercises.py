#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 7 exercises.

###############################################################################
# chapter7_exercises.py
#
# Revision:     1.00
# Date:         7/02/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 7 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
from textbook_src.exceptions import Empty
from textbook_src.ch07.doubly_linked_base import _DoublyLinkedBase
from textbook_src.ch07.linked_queue import LinkedQueue
from textbook_src.ch07.circular_queue import CircularQueue
from textbook_src.ch07.positional_list import PositionalList


# %% Reinforcement Exercises
class SinglyLinkedList:
    """Solution to exercise R-7.1.

    Give an algorithm for finding the second-to-last node in a singly linked
    list in which the last node is indicated by a next reference of None.
    """

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, n_next):    # initialize node's fields
            self._element = element             # reference to user's element
            self._next = n_next                 # reference to next node

    # ------------------------------- SLL methods -----------------------------
    def __init__(self):
        """Create an empty singly linked list."""
        self._head = None                       # reference to the head node
        self._tail = None                       # reference to the tail node
        self._size = 0                          # number of list elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def head(self):
        """Return the element at the head of the list."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def tail(self):
        """Return the element at the tail of the list."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._tail._element

    def pop(self):
        """Remove and return the element at the head of the list."""
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next           # bypass the former top node
        self._size -= 1
        return answer

    def add_first(self, e):
        """Create new node storing element e at head of list."""
        newest = self._Node(e, self._head)
        if self.is_empty():
            self._tail = newest
        self._head = newest
        self._size += 1

    def add_last(self, e):
        """Create new node storing element e at tail of list."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def traverse(self, idx):
        """Traverse the list to the node at the specified index.

        Return the node's element.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        if not 0 <= idx < self._size:  # Valid indices between 0 and n-1
            raise IndexError('Invalid index!')
        desired_node = self._head
        for _ in range(idx):
            desired_node = desired_node._next
        return desired_node._element

    def get_node(self, idx):
        """Traverse list and returns node at index."""
        if self.is_empty():
            raise Empty('Stack is empty')
        if not 0 <= idx < self._size:  # Valid indices between 0 and n-1
            raise IndexError('Invalid index!')
        desired_node = self._head
        for _ in range(idx):
            desired_node = desired_node._next
        return desired_node


def concat_sll1(L_head, M_head):
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
    # Method 1: Do not create new nodes
    L_prime = SinglyLinkedList()
    # Check if L or M are empty before attempting to concatenate
    if L_head is None and M_head is not None:
        L_head, M_head = M_head, L_head  # Swap order so code below works
    elif L_head is None and M_head is None:
        return L_prime
    L_prime._head = L_head
    L_prime._tail = L_head
    L_prime._size = 1
    node = L_prime._head
    finished_l = False  # Flag once we have reached end of list L
    while node is not None:
        if node._next is None and not finished_l:
            node._next = M_head
            finished_l = True  # Finished list L, now traversing list M
        if node._next is not None:
            L_prime._size += 1
        L_prime._tail = node
        node = node._next
    return L_prime


def concat_sll2(L_head, M_head):
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
    # Method 2: Do not modify L or M; create new nodes for L_prime
    L_prime = SinglyLinkedList()

    def add_nodes(node):
        while node is not None:
            L_prime.add_last(node._element)
            node = node._next

    add_nodes(L_head)
    add_nodes(M_head)
    return L_prime


def recursive_node_count(sll):
    """Solution to exercise R-7.3.

    Describe a recursive algorithm that counts the number of nodes in a singly
    linked list.
    """

    def recurse(node, count):
        if node is None:  # Base case, found tail of linked list
            return count
        return recurse(node._next, count+1)

    return recurse(sll._head, 0)


class DoublyLinkedList(_DoublyLinkedBase):
    """A full doubly linked list implementation."""

    def head(self):
        """Return the element at the head of the list."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._header._next._element

    def tail(self):
        """Return the element at the tail of the list."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._trailer._prev._element

    def delete_first(self):
        """Remove and return the element at the head of the list."""
        if self.is_empty():
            raise Empty('Stack is empty')
        head_node = self._header._next
        answer = head_node._element
        self._header._next = head_node._next      # bypass the former head node
        self._size -= 1
        return answer

    def delete_last(self):
        """Remove and return the element at the tail of the list."""
        if self.is_empty():
            raise Empty('Stack is empty')
        tail_node = self._trailer._prev
        answer = tail_node._element
        self._trailer._prev = tail_node._prev     # bypass the former tail node
        self._size -= 1
        return answer

    def add_first(self, e):
        """Create new node storing element e at head of list."""
        newest = self._Node(e, self._header, self._header._next)
        self._header._next._prev = newest  # Previous head's _prev is new node
        self._header._next = newest        # Header points to new node
        self._size += 1

    def add_last(self, e):
        """Create new node storing element e at tail of list."""
        newest = self._Node(e, self._trailer._prev, self._trailer)
        self._trailer._prev._next = newest  # Previous tail's _next is new node
        self._trailer._prev = newest        # Trailer points to new node
        self._size += 1

    def forward_traverse(self, idx):
        """Traverse the list to the node at the specified index.

        Return the node's element.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        if not 0 <= idx < self._size:  # Valid indices between 0 and n-1
            raise IndexError('Invalid index!')
        desired_node = self._header._next
        for _ in range(idx):
            desired_node = desired_node._next
        return desired_node._element

    def get_node(self, idx):
        """Traverse list and returns node at index."""
        if self.is_empty():
            raise Empty('Stack is empty')
        if not 0 <= idx < self._size:  # Valid indices between 0 and n-1
            raise IndexError('Invalid index!')
        desired_node = self._header._next
        for _ in range(idx):
            desired_node = desired_node._next
        return desired_node


def node_swap(alist, node1, node2):
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
    if isinstance(alist, SinglyLinkedList):
        node1_prev = None
        node2_prev = None
        prev_node = None
        current_node = alist._head
        # Traverse the list looking for the previous nodes for node1 and node2
        for _ in range(len(alist)):
            if current_node is node1:
                if prev_node is not None:
                    node1_prev = prev_node
            elif current_node is node2:
                if prev_node is not None:
                    node2_prev = prev_node
            prev_node = current_node
            current_node = current_node._next
        # Swap node references
        if node1_prev is not None:
            node1_prev._next = node2
        if node2_prev is not None:
            node2_prev._next = node1
        node1._next, node2._next = node2._next, node1._next
    elif isinstance(alist, DoublyLinkedList):
        # Swap references of neighbors of node1 and node2
        node1._prev._next = node2
        node1._next._prev = node2
        node2._prev._next = node1
        node2._next._prev = node1
        # Swap node1 and node2 references
        node1._prev, node2._prev = node2._prev, node1._prev
        node1._next, node2._next = node2._next, node1._next


def circular_count(circ):
    """Solution to exercise R-7.5.

    Implement a function that counts the number of nodes in a circularly
    linked list.
    """
    count = 0
    if circ.is_empty():
        return count
    current_node = circ._tail._next
    while current_node is not circ._tail:
        count += 1
        current_node = current_node._next
    return count+1


class CircularListIdentify(CircularQueue):
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

    # -------------------------------------------------------------------------
    # nested _Node class
    class _Node:
        """Override _Node class to accept list reference."""

        __slots__ = '_element', '_next', '_list'      # streamline memory usage

        def __init__(self, element, n_next, mylist):
            self._element = element
            self._next = n_next
            self._list = mylist

    # end of _Node class
    # -------------------------------------------------------------------------

    def enqueue(self, e):
        """Override enqueue method to pass self reference to node."""
        newest = self._Node(e, None, self)      # node will be new tail node
        if self.is_empty():
            newest._next = newest               # initialize circularly
        else:
            newest._next = self._tail._next     # new node points to head
            self._tail._next = newest           # old tail points to new node
        self._tail = newest                     # new node becomes the tail
        self._size += 1


class RotateLinkedQueue(LinkedQueue):
    """Solution to exercise R-7.7.

    Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
    has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty
    queue. Implement such a method for the LinkedQueue class of Section
    7.1.2 without the creation of any new nodes.
    """

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            # First, find the node directly before the tail
            node_before_tail = None
            current_node = self._head
            for _ in range(self._size):
                if current_node._next is self._tail:
                    node_before_tail = current_node
                current_node = current_node._next
            # Set the node before the tail to point to the head node
            node_before_tail._next = self._head
            # Set the tail to point to the head's next node
            self._tail._next = self._head._next
            self._head._next = None  # Head now points at None
            # Swap the head and tail references in the list
            self._tail, self._head = self._head, self._tail


def find_middle_node(doubly):
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
    if doubly.is_empty():
        return None
    node = doubly._header
    for _ in range((doubly._size-1) // 2 + 1):  # Upper limit excluded, so +1
        node = node._next
    return node


def concat_dll(L, M):
    """Solution to exercise R-7.9.

    Give a fast algorithm for concatenating two doubly linked lists L and M,
    with header and trailer sentinel nodes, into a single list L'.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I assume for this exercise that L and M can be modified, and that L' should
    refer to the original nodes (not create new ones).
    """
    L_prime = DoublyLinkedList()
    L_prime._header = L._header
    L_prime._trailer = M._trailer
    L_prime._size = L._size + M._size
    L_tail = L._trailer._prev
    M_head = M._header._next
    L_tail._next = M_head
    M_head._prev = L_tail
    return L_prime


def positional_adt():
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
    return True


def pl_max(pos_list):
    """Solution to exercise R-7.11.

    Implement a function, with calling syntax max(L), that returns the max-
    imum element from a PositionalList instance L containing comparable
    elements.
    """
    max_val = pos_list.first().element()
    for element in pos_list:
        if element > max_val:
            max_val = element
    return max_val


class PositionalListMax(PositionalList):
    """Solution to exercise R-7.12.

    Redo the previously problem with max as a method of the PositionalList
    class, so that calling syntax L.max( ) is supported.
    """

    def max(self):
        """Return maximum element of positional list."""
        max_val = self.first().element()
        for element in self:
            if element > max_val:
                max_val = element
        return max_val


class PositionalListFind(PositionalList):
    """Solution to exercise R-7.13.

    Update the PositionalList class to support an additional method find(e),
    which returns the position of the (first occurrence of ) element e in the
    list (or None if not found).
    """

    def find(self, find_e):
        """Return position of first occurrence of element e.

        Return None if element not found.
        """
        cursor = self.first()
        while cursor is not None:
            if cursor.element() == find_e:
                return cursor
            cursor = self.after(cursor)
        return None


class PositionalListRecursiveFind(PositionalList):
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

    def find(self, find_e):
        """Return position of first occurrence of element e.

        Return None if element not found.
        """

        def recurse(cursor):
            if cursor is None:
                return cursor  # Base case, element not found in list
            if cursor.element() == find_e:
                return cursor  # Base case, element found
            return recurse(self.after(cursor))

        return recurse(self.first())


class PositionalListReverse(PositionalList):
    """Solution to exercise R-7.15.

    Provide support for a reversed method of the PositionalList class that
    is similar to the given iter, but that iterates the elements in reversed
    order.
    """

    def reverse(self):
        """Generate a reverse iteration of the elements of the list."""
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)


def mtf_order():
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
    return ('e', 'd', 'b', 'f', 'c', 'a')


def reverse_mtf(mtf, n):
    """Solution to exercise R-7.20.

    Let L be a list of n items maintained according to the move-to-front
    heuristic. Describe a series of O(n) accesses that will reverse L.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Access each member of the list in the reverse of the current order.
    This is an O(n) method that will reverse the order of the list.
    """
    # Reverse elements in list
    for x in range(n-1, -1, -1):  # Access each element in reverse
        mtf.access(x)
