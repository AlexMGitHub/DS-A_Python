"""Graph class for directed and undirected graphs.

###############################################################################
# graph_data_structures.py
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
#   Graph: Class to implement a graph using an adjacency map.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
from interview.array_data_structures import Map


# %% Classes
class Graph:
    """Class to implement a graph using an adjacency map."""

    class _Vertex:
        """Hashable vertex that stores an element."""

        __slots__ = '_element',

        def __init__(self, element):
            """Store reference to an element."""
            self._element = element

        def element(self):
            """Return stored element."""
            return self._element

        def __hash__(self):
            """Return hash code computed using Vertex object."""
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
            """Return hash code computed using Edge object."""
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

    def is_directed(self):
        """Return True if graph is directed, False if undirected."""
        return self._directed

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

        Return the edge's element.
        """
        u = edge._origin
        v = edge._destination
        del self._outgoing_map[u][v]
        del self._incoming_map[v][u]
        return edge.element()
