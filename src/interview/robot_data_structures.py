"""Classes used to solve robot path programming test.

###############################################################################
# robot_data_structures.py
#
# Revision:     1.00
# Date:         7/22/2021
# Author:       Alex
#
# Purpose:      Implementations of various data structures used to solve the
#               robot programming exercise.
#
###############################################################################
"""

# %% Imports
# Standard system imports
from collections.abc import Hashable

# Related third party imports
import numpy as np

# Local application/library specific imports


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
            return not (self == other)

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
        """Delete item associated with key.  Raise key error if not found."""
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
        """Returns compressed hash code calculated using 5-bit cyclic shift.

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
        """Deletes a node and re-links the list.  Returns node's element."""
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
        """Return first position in list. Raise ValueError if list is empty."""
        if not self.is_empty():
            return self._wrap_node(self._header._next)
        raise ValueError('List is empty!')

    def last(self):
        """Return last position in list.  Raise ValueError if list is empty."""
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


class Graph:
    """Class to implement a graph using an adjacency map."""

    class _Vertex:
        """Hashable vertex that stores an element."""
        __slots__ = '_element',

        def __init__(self, element):
            """Stores reference to an element."""
            self._element = element

        def element(self):
            """Returns stored element."""
            return self._element

        def __hash__(self):
            """Returns hash code computed using Vertex object."""
            return hash(id(self))

    class _Edge:
        """Hashable edge that stores its endpoint vertices and an element."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, origin, destination, element):
            """Store endpoints of edge and the edge's element."""
            self._origin = origin
            self._destination = destination
            self._element = element

        def element(self):
            """Return edge's element."""
            return self._element

        def endpoints(self):
            """Return tuple containing endpoints u and v."""
            return (self._origin, self._destination)

        def opposite(self, vertex):
            """Return endpoint opposite vertex."""
            if vertex is self._origin:
                return self._destination
            if vertex is self._destination:
                return self._origin
            raise ValueError('Vertex is not an endpoint of edge!')

        def __hash__(self):
            """Returns hash code computed using Edge object."""
            return hash(id(self))

    def __init__(self, directed=False):
        """Initialize a graph implemented as an adjacency map.

        Graph can be defined as either directed (True) or undirected (False).
        By default the graph is undirected.

        The adjacency map is implemented as a map of maps, where the keys are
        vertices and the values are secondary maps.  The secondary maps contain
        adjacent vertices as keys and incident edges as values.

        The adjacency map is split into two separate maps for directed graphs;
        and incoming map for incoming edges and an outgoing map for outgoing
        edges.  For undirected graphs, the incoming map is simply set as an
        alias to the outgoing map.
        """
        self._directed = directed
        self._outgoing_map = Map()
        if directed:
            self._incoming_map = Map()
        else:
            self._incoming_map = self._outgoing_map

    def vertex_count(self):
        """Return number of vertices in the graph."""
        return len(self._outgoing_map)

    def vertices(self):
        """Return an iteration of all vertices in the graph."""
        for vertex, _ in self._outgoing_map:
            yield vertex

    def edge_count(self):
        """Return the number of edges in the graph."""
        edges = sum(len(self._outgoing_map[v]) for v, _ in self._outgoing_map)
        if self._directed:
            return edges
        return edges // 2  # Divide by two to prevent double-counting edges

    def edges(self):
        """Return a set of all edges in the graph.

        A set ensures that edges aren't double-counted.
        """
        edges = set()
        for _, edge_map in self._outgoing_map:
            for _, edge in edge_map:
                edges.add(edge)
        return edges

    def get_edge(self, u, v):
        """Return the edge from u to v, if it exists; otherwise return None.

        The order of u and v do not make a difference for an undirected graph.
        """
        return self._outgoing_map[u].get(v)  # Return None if does not exist

    def degree(self, v, out=True):
        """Return number of edges incident to vertex v for an undirected graph.

        For a directed graph, return number of either incoming or outcoming
        edges as determined by the optional argument.
        """
        if out:
            return len(self._outgoing_map[v])
        return len(self._incoming_map[v])

    def incident_edges(self, v, out=True):
        """Return an iteration of edges incident to vertex v.

        For an undirected graph this will be all incident edges, for a directed
        graph it will be either incoming or outgoing edges as determined by the
        optional argument.
        """
        if out:
            edges_map = self._outgoing_map[v]
        else:
            edges_map = self._incoming_map[v]
        for _, edge in edges_map:
            yield edge

    def insert_vertex(self, element=None):
        """Create and return a new Vertex storing an element."""
        vertex = self._Vertex(element)
        self._outgoing_map[vertex] = Map()
        if self._directed:
            self._incoming_map[vertex] = Map()
        return vertex

    def insert_edge(self, u, v, element=None):
        """Create and return new edge from vertex u to v.

        Edge can optionally store an element.
        """
        edge = self._Edge(u, v, element)
        self._outgoing_map[u][v] = edge
        self._incoming_map[v][u] = edge
        return edge

    def remove_vertex(self, v):
        """Remove vertex v and all its incident edges from the graph.

        Deleting v from the incoming/outgoing maps will delete its references
        to its edges.  However, the endpoints of those edges will still have
        references to the (now invalid) edges in their secondary maps.

        To completely remove v's edges, first access the secondary map
        containing v's outgoing edges.  Then iterate through all of the edges'
        destination vertices in the incoming map and delete their references to
        v.

        If the graph is directed, next access the secondary map containing v's
        incoming edges.  Then iterate through all of the edges' origin vertices
        in the outgoing map and delete their references to v.

        Return the vertex's element.
        """
        for destination, _ in self._outgoing_map[v]:
            del self._incoming_map[destination][v]
        del self._outgoing_map[v]
        if self._directed:
            for origin, _ in self._incoming_map[v]:
                del self._outgoing_map[origin][v]
            del self._incoming_map[v]
        return v.element()

    def remove_edge(self, edge):
        """Remove edge from the graph.

        Return the edge's element."""
        u = edge._origin
        v = edge._destination
        del self._outgoing_map[u][v]
        del self._incoming_map[v][u]
        return edge.element()


if __name__ == '__main__':
    pass
