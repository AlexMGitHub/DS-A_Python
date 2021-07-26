"""Test graph classes used to solve robot path programming test.

###############################################################################
# test_graph_data_structures.py
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
from interview.robot.graph_data_structures import Graph
from interview.robot.array_data_structures import Map


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
    # Test invalid inputs
    vert_c = graph.insert_vertex('c')
    with pytest.raises(ValueError):
        edge.opposite(vert_c)
    # Test hashing Vertex objects
    edge2 = graph.insert_edge(vert_b, vert_a, 7)
    edge_map = Map()
    edge_map[edge] = 1
    edge_map[edge2] = 2
    assert edge_map[edge] == 1
    assert edge_map[edge2] == 2


@pytest.fixture(name="g", scope="function", params=[True, False],
                ids=lambda x: f'directed={x}')
def graph_fixture(request):
    """Fixture to supply graphs to test the Graph class."""

    class GraphInit:
        """Fixture class to store graphs as instance variables."""

        def __init__(self):
            """Define graphs to be used for testing the Graph class."""
            directed = request.param            # Parameterized True/False
            rng = np.random.default_rng(55)     # Seeded random generator
            self.graph = Graph(directed)        # Directed or undirected graph
            self.n = 30                         # Number of vertices n
            self.m = 60                         # Number of edges m
            self.verts = []                     # List of vertices in graph
            for x in range(self.n):  # Add vertices to graph and store in list
                self.verts.append(self.graph.insert_vertex(x))
            self.edges = []                     # List of edges in graph
            for x in range(self.m):  # Add edges to graph and store in list
                # Randomly select 2 vertices from vertex list
                samp = rng.choice(self.verts, size=2, replace=False)
                while self._edge_exists(samp[0], samp[1]):
                    # Don't overwrite existing edge, we want m distinct edges
                    samp = rng.choice(self.verts, size=2, replace=False)
                self.edges.append(
                    self.graph.insert_edge(samp[0], samp[1], x))

        def _edge_exists(self, origin, destination):
            """Check if edge already exists in graph.

            Differentiate between directed and undirected graphs.
            """
            if self.graph.get_edge(origin, destination) is not None:
                return True
            if not self.graph.is_directed():
                if self.graph.get_edge(destination, origin) is not None:
                    return True
            return False

    return GraphInit()


def test_graph_accessor_methods(g):
    """Test accessor methods of the Graph class."""
    graph = g.graph                             # Directed or undirected graph
    n = g.n                                     # Number of vertices n
    m = g.m                                     # Number of edges m
    edges = g.edges                             # List of edges in graph
    verts = g.verts                             # List of vertices in graph
    assert graph.vertex_count() == n            # Test vertex_count()
    assert graph.edge_count() == m              # Test edge_count()
    assert len(graph.edges()) == m              # Test set returned by edges()
    u, v = edges[0].endpoints()
    assert graph.get_edge(u, v) == edges[0]     # Test get_edge()
    in_deg_sum = 0
    out_deg_sum = 0
    out_edges = []
    in_edges = []
    for vertex in graph.vertices():             # Test vertices() iteration
        out_deg_sum += graph.degree(vertex)
        in_deg_sum += graph.degree(vertex, out=False)
        out_edges.extend(list(graph.incident_edges(vertex, out=True)))
        in_edges.extend(list(graph.incident_edges(vertex, out=False)))
    if graph.is_directed():
        assert out_deg_sum == in_deg_sum == m           # Test degree()
        assert len(out_edges) == len(in_edges) == m     # Test incident_edges()
    else:
        assert out_deg_sum == in_deg_sum == 2*m         # Test degree()
        assert len(out_edges) == len(in_edges) == 2*m   # Test incident_edges()
    unequal_flag = False
    for v in verts:
        same_deg = graph.degree(v, out=True) == graph.degree(v, out=False)
        if not graph.is_directed():
            assert same_deg         # in_deg == out_deg for undirected graph
        elif not same_deg:
            unequal_flag = True
    if graph.is_directed():
        assert unequal_flag  # in_deg and out_deg should differ for some verts


def test_graph_remove_vertex(g):
    """Test remove_vertex() method of the Graph class."""
    graph = g.graph                             # Directed or undirected graph
    for vertex in list(graph.vertices()):
        graph.remove_vertex(vertex)
    assert graph.vertex_count() == 0
    assert graph.edge_count() == 0


def test_graph_remove_edge(g):
    """Test remove_edge() method of the Graph class."""
    graph = g.graph                             # Directed or undirected graph
    n = g.n                                     # Number of vertices n
    for edge in graph.edges():
        graph.remove_edge(edge)
    assert graph.vertex_count() == n
    assert graph.edge_count() == 0
    assert graph.edges() == set()
    for vertex in graph.vertices():
        assert graph.degree(vertex) == graph.degree(vertex, out=False) == 0
        assert len(list(graph.incident_edges(vertex))) == \
            len(list(graph.incident_edges(vertex, out=False))) == 0
