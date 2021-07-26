"""Linked-list data structure classes.

###############################################################################
# linked_list_data_structures.py
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
#   DoublyLinkedList: Minimal implementation of a doubly linked list.
#
#   PositionalList: Class to implement a positional list.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports


# %% Classes
class DoublyLinkedList:
    """Minimal implementation of a doubly linked list.

    This class is intended to be inherited by the PositionalList class.
    """

    class _Node:
        """Doubly-linked node containing a reference to its stored element."""

        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev_node, next_node):
            """Instantiate a doubly-linked node with a stored element."""
            self._element = element
            self._prev = prev_node
            self._next = next_node

    def __init__(self):
        """Create header and trailer sentinel nodes and link them."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._size = 0
        self._header._next = self._trailer
        self._trailer._prev = self._header

    def __len__(self):
        """Return length of doubly linked list."""
        return self._size

    def is_empty(self):
        """Return True if size of list is zero."""
        return self._size == 0

    def _insert_node(self, element, prev_node, next_node):
        """Insert a new node storing element between two existing nodes.

        Returns new node.  Does not check to ensure prev/next nodes are valid.
        """
        new_node = self._Node(element, prev_node, next_node)
        prev_node._next = new_node
        next_node._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Delete node and re-links the list.  Returns node's element."""
        prev_node = node._prev
        next_node = node._next
        prev_node._next = next_node  # Re-link list around deleted node
        next_node._prev = prev_node
        self._size -= 1
        element = node._element
        node._element = node._next = node._prev = None  # Garbage collection
        return element


class PositionalList(DoublyLinkedList):
    """Class to implement a positional list.

    All methods accepting positions will ensure that the input is a valid
    position object and the position belongs to the list.  The node wrapped
    by the position will also be checked to ensure that it is valid, otherwise
    an error is raised.

    All methods that return positions will first wrap the corresponding node
    in a Position object.
    """

    class _Position:
        """Hashable wrapper class for _Node to implement a positional list."""

        __slots__ = '_node', '_container'

        def __init__(self, node, container):
            """Position references a node and its PositionalList container."""
            self._node = node
            self._container = container

        def element(self):
            """Return the element contained by the referenced node."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other position contains same node."""
            return type(self) is type(other) and self._node is other._node

        def __ne__(self, other):
            """Return True if other position does not contain same node."""
            return not self == other

        def __hash__(self):
            """Return hash code calculated from node object."""
            return hash(id(self._node))

    def _validate_position(self, position):
        """Validate position, and return its node if valid."""
        if not isinstance(position, self._Position):
            raise TypeError('Invalid object type!')
        if position._container != self:
            raise ValueError('Position does not belong to this list!')
        if position._node._next is None:  # Valid node should reference a node
            raise ValueError('Position contains invalid node!')
        return position._node

    def _wrap_node(self, node):
        """Wrap node in a Position object.  Ensure node is not a sentinel."""
        if node is self._header or node is self._trailer:
            return None  # Sentinel nodes should not be accessed
        else:
            return self._Position(node, self)

    def first(self):
        """Return first position in list.

        Raise ValueError if list is empty.
        """
        if not self.is_empty():
            return self._wrap_node(self._header._next)
        raise ValueError('List is empty!')

    def last(self):
        """Return last position in list.

        Raise ValueError if list is empty.
        """
        if not self.is_empty():
            return self._wrap_node(self._trailer._prev)
        raise ValueError('List is empty!')

    def before(self, position):
        """Return the position immediately before position p.

        Return None if p is the first position.
        """
        node = self._validate_position(position)
        if node._prev is self._header:
            return None
        return self._wrap_node(node._prev)

    def after(self, position):
        """Return the position immediately after position p.

        Return None if p is the last position.
        """
        node = self._validate_position(position)
        if node._next is self._trailer:
            return None
        return self._wrap_node(node._next)

    def __iter__(self):
        """Return forward iterator of the elements of the list."""
        position = self.first()
        while position is not None:
            yield position.element()
            position = self.after(position)

    def add_first(self, element):
        """Insert a new element at the front of list, return the position."""
        node = self._insert_node(element, self._header, self._header._next)
        return self._wrap_node(node)

    def add_last(self, element):
        """Insert a new element at the end of list, return the position."""
        node = self._insert_node(element, self._trailer._prev, self._trailer)
        return self._wrap_node(node)

    def add_before(self, position, element):
        """Insert a new element before position p, return the new position."""
        node = self._validate_position(position)
        new_node = self._insert_node(element, node._prev, node)
        return self._wrap_node(new_node)

    def add_after(self, position, element):
        """Insert a new element after position p, return the new position."""
        node = self._validate_position(position)
        new_node = self._insert_node(element, node, node._next)
        return self._wrap_node(new_node)

    def replace(self, position, element):
        """Replace element at position with new element, return old element."""
        node = self._validate_position(position)
        old_element = node._element
        node._element = element
        return old_element

    def delete(self, position):
        """Delete position and return its element."""
        node = self._validate_position(position)
        element = self._delete_node(node)
        position._node = position._container = None  # Garbage collection
        return element
