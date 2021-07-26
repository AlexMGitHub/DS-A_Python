"""Priority queue class implemented using an array-based heap.

###############################################################################
# heap_data_structures.py
#
# Revision:     1.00
# Date:         7/22/2021
# Author:       Alex
#
# Purpose:      Implementations of various data structures used to solve the
#               robot programming exercise.
#
# Contains:
#
#   BinaryTree: A minimal binary tree class implemented using a dynamic array.
#
#   Heap: Minimal implementation of a heap.
#
#   AdaptablePriorityQueue: Class to implement an APQ using a heap.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
from interview.robot.array_data_structures import Queue


# %% Classes
class BinaryTree:
    """A minimal binary tree class implemented using a dynamic array.

    This class is intended to be inherited by a heap.
    """

    DEFAULT_CAPACITY = 10

    class _Node:
        """A node class with references to left/right children and parent."""

        __slots__ = '_element', '_index', '_container'

        def __init__(self, element, index, container):
            """Instantiate a node with array index reference and element."""
            self._element = element
            self._index = index
            self._container = container

        def element(self):
            """Return the element referenced by the node."""
            return self._element

        def __eq__(self, other):
            """Return True if other Node's element equals self's element."""
            return self.element() == other.element()

        def __ne__(self, other):
            """Return True if other Node's element does not equal self's."""
            return not self == other

        def __lt__(self, other):
            """Return True if element is less than other's element."""
            return self.element() < other.element()

        def __gt__(self, other):
            """Return True if element is greater than other's element."""
            return self.element() > other.element()

        def __le__(self, other):
            """Return True if element is less than or equal to other's."""
            return self.element() <= other.element()

        def __ge__(self, other):
            """Return True if element is greater than or equal to other's."""
            return self.element() >= other.element()

    def __init__(self):
        """Initialize an empty binary tree."""
        self._size = 0
        self._array = [None] * BinaryTree.DEFAULT_CAPACITY

    @property
    def _N(self):
        """Return length of dynamic array used to implement queue."""
        return len(self._array)

    def root(self):
        """Return root node of tree.

        Returns None if tree is empty.
        """
        return self._array[0]

    def is_root(self, node):
        """Return True if node is root of the tree."""
        self._validate_node(node)
        return node._index == 0

    def left(self, node):
        """Return left child of node if it exists.

        Return None otherwise.
        """
        self._validate_node(node)
        idx = node._index
        left_idx = 2*idx + 1
        if left_idx >= self._N:
            return None                         # Exceeds length of array
        return self._array[left_idx]

    def right(self, node):
        """Return right child of node if it exists.

        Return None otherwise.
        """
        self._validate_node(node)
        idx = node._index
        right_idx = 2*idx + 2
        if right_idx >= self._N:
            return None                         # Exceeds length of array
        return self._array[right_idx]

    def parent(self, node):
        """Return parent of node if it exists.

        Return None otherwise.
        """
        self._validate_node(node)
        idx = node._index
        if idx == 0:
            return None                         # Root node has no parent
        if idx % 2 == 0:
            return self._array[(idx-2)//2]      # Right child (even number)
        return self._array[(idx-1)//2]          # left child (odd number)

    def sibling(self, node):
        """Return sibling of node if it exists.

        Return None otherwise.
        """
        self._validate_node(node)
        if self.is_root(node):
            return None                             # Root node has no siblings
        parent = self.parent(node)
        if self.num_children(parent) == 1:
            return None                             # No siblings
        if node is self.left(parent):               # If node is left child
            return self.right(parent)               # Return right child
        return self.left(parent)                    # Else return left child

    def num_children(self, node):
        """Return count of node's children."""
        self._validate_node(node)
        count = 0
        if self.left(node) is not None:
            count += 1
        if self.right(node) is not None:
            count += 1
        return count

    def children(self, node):
        """Generate iteration of children of node."""
        self._validate_node(node)
        if self.left(node) is not None:
            yield self.left(node)
        if self.right(node) is not None:
            yield self.right(node)

    def is_leaf(self, node):
        """Return True if node has no children."""
        self._validate_node(node)
        if self.num_children(node) == 0:
            return True
        return False

    def __iter__(self):
        """Generate an iteration of all elements stored within the tree."""
        root = self.root()
        queue = Queue()
        queue.enqueue(root)
        return self._breadth_first(queue)

    def nodes(self):
        """Generate an iteration of all nodes stored within the tree."""
        root = self.root()
        queue = Queue()
        queue.enqueue(root)
        return self._breadth_first(queue, elements=False)

    def _breadth_first(self, queue, elements=True):
        """Implement a breadth-first search of the tree.

        By default returns the elements contained by the tree.  If the elements
        argument is set to False will return the Node objects of the tree.
        """
        while not queue.is_empty():
            node = queue.dequeue()
            if elements:
                yield node.element()
            else:
                yield node
            for child in self.children(node):
                queue.enqueue(child)

    def _validate_node(self, node):
        """Validate node and raise error if invalid."""
        if not isinstance(node, self._Node):
            raise TypeError('Invalid object type!')
        if node._container != self:
            raise ValueError('Node does not belong to this list!')
        if node._index < 0 or node._index >= self._size:
            raise ValueError('Invalid node!')

    def __len__(self):
        """Return number of positions in tree."""
        return self._size

    def _resize_array(self, capacity):
        """Copy tree array to new array of specified capacity."""
        old_array = self._array
        self._array = [None] * capacity
        for index in range(self._size):
            self._array[index] = old_array[index]


class Heap(BinaryTree):
    """Minimal implementation of a heap.

    This class is intended to be inherited by an adaptable priority queue.
    """

    def last_node(self):
        """Return the bottom-right-most position in heap.

        Return None if heap is empty.
        """
        return self._array[self._size-1]

    def insert_element(self, element):
        """Insert a new element into the heap.

        A node containing the new element is placed at the bottom-right-most
        position in the heap.  The position is then up-heap bubbled to its
        appropriate place to maintain the heap-order property.

        Return node of inserted element.
        """
        if self._size == 0:
            node = self._Node(element, 0, self)
            self._array[0] = node  # Add node to root of empty heap
            self._size += 1
            return self.root()
        self._size += 1
        if self._size == self._N:
            self._resize_array(self._N * 2)  # Double size of array
        node = self._Node(element, self._size-1, self)
        self._array[self._size-1] = node    # Insert new node at end of heap
        self._upheap(node)                  # Up-heap it to proper location
        return node

    def _upheap(self, node):
        """Up-heap bubble the position."""
        parent = self.parent(node)
        while parent is not None and node.element() < parent.element():
            self._swap(node, parent)        # Move node upward while key
            parent = self.parent(node)      # smaller than parent's key

    def _swap(self, node1, node2):
        """Swap locations in the heap of two nodes."""
        arr = self._array
        arr[node1._index], arr[node2._index] = arr[node2._index], \
            arr[node1._index]
        # Swap indices stored in nodes as well
        node1._index, node2._index = node2._index, node1._index

    def update_node(self, node, element):
        """Update an existing node in the heap with a new element value.

        The updated key will be bubbled to its final position.

        Return updated node.
        """
        self._validate_node(node)
        node._element = element
        parent = self.parent(node)
        if parent and node.element() < parent.element():
            self._upheap(node)              # New key is smaller than parent
        else:
            self._downheap(node)            # Could be larger than child key
        return node

    def remove_min(self):
        """Remove and return the minimum position from the heap.

        To maintain the complete binary tree property, the bottom-right-most
        position will be swapped with the root, which contains the minimum key.
        The swapped position will then be down-heap bubbled to its appropriate
        position in the tree to maintain the heap-order property.

        Return element of root.
        """
        if self._size == 1:                     # Only root node in heap
            return self._delete_node(self.root())
        min_node = self._array[0]               # Root node has min value
        last = self._array[self._size-1]        # Bottom-right-most node
        self._swap(min_node, last)              # Move last node to root
        element = self._delete_node(min_node)   # Delete root
        self._downheap(last)                    # Down-heap bubble last node
        if self._size == self._N//4 and self._N > BinaryTree.DEFAULT_CAPACITY:
            self._resize_array(self._N // 2)    # Halve size of array
        return element

    def _downheap(self, node):
        """Down-heap bubble the node."""
        num_children = self.num_children(node)
        while num_children > 0:
            if num_children == 2:
                if self.right(node).element() < self.left(node).element():
                    child = self.right(node)    # Pick child with minimal key
                else:
                    child = self.left(node)
            else:
                child = self.left(node)         # Only child must be left child
            if node.element() > child.element():
                self._swap(node, child)         # Continue down-heap bubble
                num_children = self.num_children(node)
            else:
                return                          # Terminate loop

    def _delete_node(self, node):
        """Remove all references to node in the heap.

        Return element of deleted node.
        """
        element = node.element()
        self._array[node._index] = None  # Delete node from array
        node._element = node._index = node._container = None
        self._size -= 1  # Delete node references and reduce size
        return element


class AdaptablePriorityQueue(Heap):
    """Class to implement an adaptable priority queue using a heap."""

    class _Item:
        """Class to contain key and value for priority queue elements."""

        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            """Initialize Item with key-value pair."""
            self._key = key
            self._value = value

        def key(self):
            """Return Item's key."""
            return self._key

        def value(self):
            """Return Item's value."""
            return self._value

        def __eq__(self, other):
            """Return True if other Item's key equals self's key."""
            return self._key == other._key

        def __ne__(self, other):
            """Return True if other Item's key does not equal self's key."""
            return not self == other

        def __lt__(self, other):
            """Return True if key is less than other's key."""
            return self._key < other._key

        def __gt__(self, other):
            """Return True if key is greater than other's key."""
            return self._key > other._key

        def __le__(self, other):
            """Return True if key is less than or equal to other's key."""
            return self._key <= other._key

        def __ge__(self, other):
            """Return True if key is greater than or equal to other's key."""
            return self._key >= other._key

    def enqueue(self, key, value):
        """Add value to queue at location determined by key priority."""
        item = self._Item(key, value)
        node = self.insert_element(item)
        return node

    def dequeue(self):
        """Remove and return element from the front of the queue.

        Raise ValueError if queue is empty.
        """
        if self.is_empty():
            raise ValueError('Queue is empty!')
        item = self.remove_min()
        return item.key(), item.value()

    def update(self, node, key, value):
        """Update node with new key and value."""
        item = self._Item(key, value)
        self.update_node(node, item)

    def first(self):
        """Return (but do not remove) element at the front of the queue.

        Raise ValueError if queue is empty.
        """
        if self.is_empty():
            raise ValueError('Queue is empty!')
        return self.root().element().value()

    def last(self):
        """Return (but do not remove) element at the back of the queue.

        Raise ValueError if queue is empty.
        """
        if self.is_empty():
            raise ValueError('Queue is empty!')
        return self.last_node().element().value()

    def is_empty(self):
        """Return True if queue is empty."""
        return self._size == 0
