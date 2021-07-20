#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 14 exercises.

###############################################################################
# chapter14_exercises.py
#
# Revision:     1.00
# Date:         7/17/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 14 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports


# %% Reinforcement Exercises
def draw_simple_undirected_graph():
    r"""Solution to exercise R-14.1.

    Draw a simple undirected graph G that has 12 vertices, 18 edges, and 3
    connected components.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    To solve this exercise, we need to know the following definitions:

    1. A graph is simple if it does not have parallel edges or self-loops.
        a. Parallel undirected edges have the same end points
        b. A self-loop occurs if the edge connects a vertex to itself

    2. A graph is undirected if all of the edges in graph G are undirected
        a. An undirected edge (u, v) is an unordered pair (u, v)

    3. If a graph G is not connected, its maximal connected subgraphs are
       called the connected components of G
        a. A subgraph of a graph G is a graph H whose vertices and edges are
           subsets of the vertices and edges of G, respectively
        b. A graph is connected if, for any two vertices, there is a path
           between them

    And so G will be composed of three connected subgraphs - groups of vertices
    that are connected to all other vertices in the same group, but not to the
    vertices in other groups:

       1           5            9
     / | \       / | \        / | \
    2--+--3     6--+--7     10--+--11
     \ | /       \ | /        \ | /
       4           8            12

    I've numbered the vertices 1 through 12.  Each of the three connected
    components consists of 4 vertices and 6 edges, for a total of 12 vertices
    and 18 edges.  Within each subgraph there is a path between any two
    vertices, meaning that the subgraphs are indeed connected components.
    In addition, G is simple as there are no parallel edges or self-loops.

    This satisfies the requirements of the exercise.
    """
    return True


def largest_number_of_edges():
    """Solution to exercise R-14.2.

    If G is a simple undirected graph with 12 vertices and 3 connected com-
    ponents, what is the largest number of edges it might have?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    According to Proposition 14.10, a simple undirected graph G with n vertices
    must have m <= n(n-1)/2 edges.

    Technically, a subgraph consisting of 1 vertex is connected.  Knowing this,
    we can maximize m by putting 10 vertices in one connected component, and a
    single vertex in the other two connected components.  These latter two
    connected components will have zero edges, and so the largest number of
    edges is thus m for n = 10:

    m <= 10*(10-1)/2
    m <= 10*9/2
    m <= 90/2
    m <= 45

    The largest number of edges is 45.
    """
    return True


def draw_adjacency_matrix():
    """Solution to exercise R-14.3.

    Draw an adjacency matrix representation of the undirected graph shown
    in Figure 14.1.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    First, I will label each edge in Figure 14.1 with a letter as follows:

    Snoeyink    ---     Goodrich    a
    Garg        ---     Goodrich    b
    Garg        ---     Tamassia    c
    Goldwasser  ---     Goodrich    d
    Goldwasser  ---     Tamassia    e
    Goodrich    ---     Tamassia    f
    Goodrich    ---     Vitter      g
    Goodrich    ---     Chiang      h
    Tamassia    ---     Tollis      i
    Tamassia    ---     Vitter      j
    Tamassia    ---     Preparata   k
    Tamassia    ---     Chiang      l
    Tollis      ---     Vitter      m
    Vitter      ---     Preparata   n
    Preparata   ---     Chiang      o


                         0   1   2   3   4   5   6   7   8
    Snoeyink    --> 0  |   |   |   | a |   |   |   |   |   |
    Garg        --> 1  |   |   |   | b | c |   |   |   |   |
    Goldwasser  --> 2  |   |   |   | d | e |   |   |   |   |
    Goodrich    --> 3  | a | b | d |   | f |   | g |   | h |
    Tamassia    --> 4  |   | c | e | f |   | i | j | k | l |
    Tollis      --> 5  |   |   |   |   | i |   | m |   |   |
    Vitter      --> 6  |   |   |   | g | j | m |   | n |   |
    Preparata   --> 7  |   |   |   |   | k |   | n |   | o |
    Chiang      --> 8  |   |   |   | h | l |   |   | o |   |

    Note that the array is symmetric (A[i,j] == A[j,i]) as expected for an
    undirected graph.
    """
    return True


def draw_adjacency_list():
    """Solution to exercise R-14.4.

    Draw an adjacency list representation of the undirected graph shown in
    Figure 14.1.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    I will re-use the edge labels from Exercise R-14.3:

    Snoeyink    ---     Goodrich    a
    Garg        ---     Goodrich    b
    Garg        ---     Tamassia    c
    Goldwasser  ---     Goodrich    d
    Goldwasser  ---     Tamassia    e
    Goodrich    ---     Tamassia    f
    Goodrich    ---     Vitter      g
    Goodrich    ---     Chiang      h
    Tamassia    ---     Tollis      i
    Tamassia    ---     Vitter      j
    Tamassia    ---     Preparata   k
    Tamassia    ---     Chiang      l
    Tollis      ---     Vitter      m
    Vitter      ---     Preparata   n
    Preparata   ---     Chiang      o

    The adjacency list V is a list of vertices v that each point to a
    collection I(v) that contains the incident edges of v.

    Snoeyink    -->     {a}
    Garg        -->     {b, c}
    Goldwasser  -->     {d, e}
    Goodrich    -->     {a, b, d, f, g, h}
    Tamassia    -->     {c, e, f, i, j, k, l}
    Vitter      -->     {g, j, m, n}
    Chiang      -->     {h, l, o}
    Tollis      -->     {i, m}
    Preparata   -->     {k, n, o}

    Note that each edge appears twice in the adjacency list, for a total of
    2*m = 2*15 = 30 edges.
    """
    return True


def draw_euler_tour():
    r"""Solution to exercise R-14.5.

    Draw a simple, connected, directed graph with 8 vertices and 16 edges
    such that the in-degree and out-degree of each vertex is 2. Show that there
    is a single (nonsimple) cycle that includes all the edges of your graph,
    that is, you can trace all the edges in their respective directions without
    ever lifting your pencil. (Such a cycle is called an Euler tour.)

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A simple graph contains no parallel edges or self-loops.  For a directed
    graph, parallel edges are those that have the same origin and destination
    vertices.  The in-degree and out-degree of a vertex indicates how many
    incoming and outgoing edges are connected to the vertex, respectively.
    A simple cycle is a path that starts and ends at the same vertex, but all
    other vertices in the cycle are distinct.  A graph is connected if, for
    any two vertices, there is a path between them.

            1     2
            ↓ ↘ ↙ ↓     a, b, c, d
            ↓ ↙ ↘ ↓
            3     4
            ↓ ↘ ↙ ↓     e, f, g, h
            ↓ ↙ ↘ ↓
            5     6
            ↓ ↘ ↙ ↓     i, j, k, l
            ↓ ↙ ↘ ↓
            7     8
            ↓ ↘ ↙ ↓     m, n, o, p
            ↓ ↙ ↘ ↓
            1*    2*

    The graph above has 8 vertices labeled 1 through 8 and 16 edges labeled
    (left to right) a through p.  Due to the limitations of drawing using text,
    I represent vertices 7 and 8 wrapping around to vertices 1 and 2 by
    redrawing 1* and 2* below 7 and 8.  The asterisks indicate that these are
    references to the vertices 1 and 2, respectively.

    Each vertex has two outgoing edges and two incoming edges, making them
    indeg(2) and outdeg(2).  There are no parallel edges as each edge has a
    distinct pair of origin and destination vertices.  There are no self-loops,
    as no vertex has an edge pointing to itself.  The graph is connected as
    there is a path between any two vertices in the graph.

    The final requirement is that there be a single non-simple cycle that
    includes all of the edges of the graph.  A non-simple cycle allows vertices
    to be repeated in the path of the cycle:

    P = (1, 4, 5, 8, 2, 3, 6, 7, 1, 3, 5, 7, 2, 4, 6, 8, 1)
    P = (b, g, j, p, c, f, k, m, a, e, i, n, d, h, l, o)

    I've written the path in terms of vertices and again in terms of edges.
    From the vertices representation of the path it's clear that the cycle
    starts and ends at the same vertex 1.  Each vertex in the path is repeated
    twice except for vertex 1, which is repeated three times as it is the
    (arbitrary) start and end of the cycle.  This makes sense as each vertex
    has indeg(2) and outdeg(2), which requires that every vertex be traversed
    twice to cover each edge connected to it.

    The edge representation of the cycle verifies that all 16 distinct edges of
    the graph are included in the path, thus meeting the requirements of the
    exercise.
    """
    return True


def edge_list_time():
    """Solution to exercise R-14.6.

    Suppose we represent a graph G having n vertices and m edges with the
    edge list structure. Why, in this case, does the insert vertex method run
    in O(1) time while the remove vertex method runs in O(m) time?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The edge list structure represents the vertices and edges of a graph in two
    unordered lists V and E, respectively.  Both V and E are implemented as
    positional lists, which allow new positions to be added in O(1) time.
    An edge stored in E contains references to its two endpoints, u and v.
    But a vertex stored in V does not contain references to its edges.

    Because of this, a new vertex can be added to V in O(1) time as it does not
    require any searching through E prior to adding the new vertex.  Edges that
    are incident to a vertex v will be added separately using the insert_edge()
    method.

    However, when removing a vertex v from the graph its incident edges must
    also be removed.  Because a vertex in list V does not contain any
    references to v's incident edges, list E must be exhaustively searched to
    find and delete all edges incident to vertex v.  As the graph has m edges
    this will require O(m) time.
    """
    return True


def insert_edge_matrix():
    """Solution to exercise R-14.7.

    Give pseudo-code for performing the operation insert_edge(u, v, x) in O(1)
    time using the adjacency matrix representation.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    An adjacency matrix representation of a graph G of n vertices and m edges
    uses an (n x n) array A to store references to the edges of any two
    vertices (u, v).

    Each vertex is associated with an integer in the range [0, n-1] that
    represents its row and column number in A.  I implement this as a
    dictionary to map vertex to integer for expected O(1) time look-ups.  The
    index i is associated with vertex u and the index j is associated with
    vertex v.  Assigning a value x to A[i,j] is also O(1) time.

    If an edge between vertices u and v does not exist in G, then the
    corresponding entry in A will be None.  If the edge does exist, querying A
    will return a reference to the associated Edge instance.

    Finally, if G is undirected then A[i,j] == A[j,i].  I handle this scenario
    with a conditional statement that will also run in O(1) time.


    def insert_edge(u, v, x):
        i = vertex_dict[u]          # Look up index associated with vertex u
        j = vertex_dict[v]          # Look up index associated with vertex v
        if A[i, j] is not None:
            raise ValueError('u and v already adjacent')
        e = Edge(u, v, x)           # Create Edge instance
        A[i, j] = e                 # Store reference to edge in array
        if G is not directed:       # A is symmetric for undirected graphs
            A[j, i] = e


    The above pseudocode should run in expected O(1) time.
    """
    return True


def insert_edge_list():
    """Solution to exercise R-14.8.

    Repeat Exercise R-14.7 for the adjacency list representation, as described
    in the chapter.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    An adjacency list uses a primary list structure V to store the vertices of
    graph G.  V is implemented as a positional list, where each vertex v
    contains a reference to a secondary list I(v) which contains all of v's
    incident edges.  A directed list will have a I_incoming and I_outgoing to
    distinguish between incoming and outgoing edges.  An undirected list will
    simply have I_incoming point to I_outgoing and thus use one list to keep
    track of edges.

    If I assume that I_incoming and I_outgoing are implemented as positional
    lists as well, then a new edge can be added to these lists in O(1) time.
    Even if they are implemented as Python lists the append operation is O(1)
    amortized.

    I do not implement error checking in the pseudocode below, because the
    get_edge(u, v) method requires O(min(deg(u), deg(v))) time  to iterate
    through the secondary lists and would prevent the insert_edge() method from
    being O(1) time.


    def insert_edge(u, v, x):
        e = Edge(u, v, x)               # Create edge instance
        u.I_outgoing.add_last(e)        # Add edge to outgoing list of u
        v.I_incoming.add_last(e)        # Add edge to incoming list of v


    The above pseudocode should run in O(1) time.
    """
    return True


def omit_edge_list():
    """Solution to exercise R-14.9.

    Can edge list E be omitted from the adjacency matrix representation while
    still achieving the time bounds given in Table 14.1? Why or why not?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    An adjacency matrix stores references to each edge in the graph in an
    (n x n) array, where each vertex v is numbered with an integer [0, n-1].
    Let's go through each method in Table 14.1 and see if we can still maintain
    the stated time bounds without an unordered list of edges, E:

    1. vertex_count(), O(1):
        This is simply n, and does not require an edge list.

    2. edge_count(), O(1):
        The edge list would typically store this value as an instance variable.
        We could still achieve O(1) time if a similar instance variable is
        stored in the adjacency matrix and incremented/decremented whenever
        an edge is added or deleted.

    3. vertices(), O(n):
        Iteration through vertices, unaffected by lack of edge list.

    4. edges(), O(m):
        Iteration through edges.  Without an edge list to iterate through,
        we would need to iterate through the entire (n x n) adjacency array
        to return every edge in the graph.  This would require O(n^2) time.
        According to Proposition 14.10, the number of edges in a simple graph
        with n vertices is also O(n^2).  However, as noted in the text most
        real-world graphs are sparse, meaning that the number of edges will not
        be proportional to n^2.  This means that iterating through the entire
        adjacency array would usually be slower than iterating through the
        edge list.  We can state that it is not guaranteed that we can achieve
        the same time bounds for the edges() method without an edge list.

    5.  get_edge(u,v), O(1):
        We can still get the edge between vertex u and v in constant time
        without an edge list.  The vertices u and v are associated with
        integers i and j that can be used to access the edge stored at A[i,j]
        in the adjacency matrix.  The vertices can either directly store their
        associated integer, or the integers can be stored in a map associated
        with their respective vertex.  In either case, we can achieve O(1)
        run-time efficiency without an edge list.

    6.  degree(v), O(n):
        This method works by iterating through the row of the array associated
        with v.  It is unaffected by the existence of an edge list.

    7.  incident_edges(v), O(n):
        This method also iterates through the cells of the row of the array
        associated with v, and is unaffected by the existence of an edge list.

    8.  insert_vertex(x), O(n^2);
        Requires copying the contents of the existing array to a larger array.
        Unaffected by the existence of an edge list.

    9.  remove_vertex(v), O(n^2):
        Requires copying the contents of the existing array to a smaller array.
        Unaffected by the existence of an edge list.

    10. insert_edge(u,v,x), O(1):
        Given O(1) time to look up the integers associated with vertices u and
        v, the insert_edge() method can insert a new edge into the array in
        O(1) time without an edge list.

    11. remove_edge(e), O(1):
        The edge object contains references to its endpoints u and v, which can
        then be used to look up their corresponding integers in O(1) time.
        Then the array can be updated so that A[i,j] = None.  This can all be
        done in O(1) time without an edge list.

    In conclusion, it seems that all of the methods of the adjacency matrix can
    maintain their stated time bounds without an edge list E except for the
    edges() method.  Without an edge list to iterate through, we cannot
    guarantee O(m) performance for this method.
    """
    return True


def omit_edge_list2():
    """Solution to exercise R-14.10.

    Can edge list E be omitted from the adjacency list representation while
    still achieving the time bounds given in Table 14.3? Why or why not?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    According to the text, without an auxillary list E of edges the edges()
    method requires O(n + m) time to access each secondary list in each of n
    vertices and report its edges.  This is worse than the O(m) time bound with
    an edge list E.

    In addition, the edge_count() method runs in O(1) time with an edge list E,
    but would require O(n) time to access the length of each secondary list in
    all n vertices of the graph.

    In conclusion, if the edge list E is omitted from the adjacency list
    representation of a graph it is not possible to achieve the time bounds
    given in Table 14.3.
    """
    return True


def list_or_matrix():
    """Solution to exercise R-14.11.

    Would you use the adjacency matrix structure or the adjacency list struc-
    ture in each of the following cases? Justify your choice.

    a. The graph has 10,000 vertices and 20,000 edges, and it is important
       to use as little space as possible.

    b. The graph has 10,000 vertices and 20,000,000 edges, and it is im-
       portant to use as little space as possible.

    c. You need to answer the query get_edge(u,v) as fast as possible, no
       matter how much space you use.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    a. The adjacency list's memory usage is O(n + m), while the adjacency
       matrix's memory usage is O(n^2).  This means the list will use O(30,000)
       memory, while the matrix will use O(100,000,000) memory.  The adjacency
       list is the preferred choice as it uses less space.

    b. In this case the adjacency list uses O(20,010,000) memory, and the
       adjacency matrix uses O(100,000,000) memory.  The adjacent list is still
       the preferred choice as it uses less memory.

    c. The method get_edge(u,v) runs in O(min(deg(u), deg(v))) time for the
       adjacency list, and O(1) time for the adjacency matrix.  The adjacency
       matrix is the preferred choice as it is faster and its space usage is
       considered irrelevant.
    """
    return True


def dfs_traversal_matrix():
    """Solution to exercise R-14.12.

    Explain why the DFS traversal runs in O(n^2) time on an n-vertex simple
    graph that is represented with the adjacency matrix structure.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A depth-first search visits each vertex no more than once, and for each
    vertex calls the incident_edges() method of the graph to iterate through
    all edges connected to the vertex.  The incident_edges() method runs in
    O(n) time for an adjacency matrix representation, and since there are n
    vertices DFS is thus O(n^2) for an adjacency matrix structure.
    """
    return True


def dfs_complete_graph():
    r"""Solution to exercise R-14.14.

    A simple undirected graph is complete if it contains an edge between every
    pair of distinct vertices. What does a depth-first search tree of a
    complete graph look like?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A simple undirected graph will not have any self-loops or parallel edges.
    Every vertex is connected to every other vertex in the graph.  Because of
    this, the DFS will never need to backtrack to find an undiscovered vertex.
    The only dead end that the search will encounter is when every vertex has
    been discovered, and only then will it backtrack to the starting vertex.

    Because it is an undirected tree, all of the non-tree edges of the DFS tree
    will be back edges; that is edges connected to ancestors.  The search tree
    itself will consist of a straight vertical line of one ancestor to one
    descendant from the root of the tree to the final vertex.

    As an example, the simple graph below has vertices numbered 1 through 4.
    Each vertex has an edge between every distinct pair of vertices.  The
    resulting depth-first search tree rooted at vertex 1 is shown below the
    graph, assuming the vertices happen to be visited in numerical order.

    Complete graph:

           1
         / | \
        2--+--3
         \ | /
           4

    DFS tree rooted at vertex 1:

        1
        |
        2
        |
        3
        |
        4
    """
    return True


def bfs_complete_graph():
    r"""Solution to exercise R-14.15.

    Recalling the definition of a complete graph from Exercise R-14.14, what
    does a breadth-first search tree of a complete graph look like?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The breadth-first search builds its tree level by level.  The starting
    vertex s is assigned to level 0, and all vertices adjacent to s are
    assigned to level 1.  However, in a complete graph *all* of the other
    vertices in the graph are adjacent to s, and so the resulting search tree
    will have a single root vertex at level 0, and then all n-1 vertices at
    level 1 of the tree.

    Complete graph:

           1
         / | \
        2--+--3
         \ | /
           4

    BFS tree rooted at vertex 1:

        1
      / | \
    2   3   4
    """
    return True


def traverse_graph_bfs_and_dfs():
    r"""Solution to exercise R-14.16.

    Let G be an undirected graph whose vertices are the integers 1 through 8,
    and let the adjacent vertices of each vertex be given by the table below:

    vertex      adjacent vertices
    1           (2, 3, 4)
    2           (1, 3, 4)
    3           (1, 2, 4)
    4           (1, 2, 3, 6)
    5           (6, 7, 8)
    6           (4, 5, 7)
    7           (5, 6, 8)
    8           (5, 7)

    Assume that, in a traversal of G, the adjacent vertices of a given vertex
    are returned in the same order as they are listed in the table above.
        a. Draw G.
        b. Give the sequence of vertices of G visited using a DFS traversal
           starting at vertex 1.
        c. Give the sequence of vertices visited using a BFS traversal starting
           at vertex 1.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    a. Representation of G:

           1
         / | \
        2--+--3
         \ | /
           4
           |
           6
         /   \
        5-----7
         \   /
           8

    b. DFS Sequence: (1, 2, 3, 4, 6, 5, 7, 8)

       DFS Tree: 1 --> 2 --> 3 --> 4 --> 6 --> 5 --> 7 --> 8

    c. BFS Sequence: (1, 2 3 4, 6, 5 7, 8)

       BFS Tree:

                1
              / | \
             2  3  4
                   |
                   6
                  / \
                 5   7
                 |
                 8
    """
    return True


def transitive_path_edges():
    r"""Solution to exercise R-14.19.

    How many edges are in the transitive closure of a graph that consists of a
    simple directed path of n vertices?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A simple directed path consists of an alternating sequence of distinct
    vertices and edges.  Each edge is incident to its predecessor and successor
    vertex.  A transitive closure creates an edge between vertex u and v
    whenever the original graph has a directed path between u and v.

    Since we are considering a directed path, there is a directed path between
    each vertex and all of its successor vertices in the path.

    Original path:                  Transitive closure of path:

    a -- b                          a -- b                       0 added edges

    a -- b -- c                     a -- b -- c                  1 added edge
                                     \_______/

    a -- b -- c -- d                a -- b -- c -- d             3 added edges
                                    \\____\__/____//

    a -- b -- c -- d -- e           a -- b -- c -- d -- e        6 added edges
                                    \\\__\\___/\__//__///


    a -- b -- c -- d -- e -- f      a -- b -- c -- d -- e -- f   10 added edges
                                   \\\\__\\\__/\\_//\__///_////


    We can see a pattern emerging: the original path has n-1 edges, and the
    transitive closure of the path adds edges equal to the sum of the first n-2
    integers.  The total number of edges in a simple directed path of n
    vertices is thus:

        (n-1) + (n-2) * ((n-2)+1) / 2
    =   (n-1) + (n-2) * (n-1) / 2
    =   (n-1) + (n^2 - 3n + 2) / 2
    =   (n-1) + 0.5n^2 - 1.5n + 1
    =   0.5n^2 - 0.5n
    =   (n^2 - n) / 2

    We can test this result on the examples above:

    1.  n = 2
        (2^2 - 2) / 2 = 1 edge
    2.  n = 3
        (3^2 - 3) / 2 = 3 edges
    3.  n = 4
        (4^2 - 4) / 2 = 6 edges
    4.  n = 5
        (5^2 - 5) / 2 = 10 edges
    5.  n = 6
        (6^2 - 6) / 2 = 15 edges

    The formula is correct.  The total number of edges in a simple directed
    path of n vertices is (n^2 - n) / 2.
    """
    return True


def topological_ordering():
    """Solution to exercise R-14.21.

    Compute a topological ordering for the directed graph drawn with solid
    edges in Figure 14.3d.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    To compute the topological ordering for G, first we will count the number
    of incoming edges for each vertice v in G.  At least one of these vertices
    must have 0 incoming edges, and these vertices are added to a "ready" list.

    The vertices in the ready list are one-by-one added to a list keeping track
    of topological order, and thus removed from G.  As the ready vertices are
    removed from G, the outgoing edges connected to their adjacent vertices are
    also removed.  If any of these adjacent vertices now have zero incoming
    edges they are added to the ready list.  The process continues until the
    ready list is empty.  The resulting topological list will contain the
    vertices in topological ordering.

    The DAG in 14.3d is as follows:

                BOS
             ↙   ↓   ↘
           ↓    JFK    ↓
           ↓ ↙   ↓   ↘ ↓
          SFO ← DFW ← MIA
                 ↑  ↘  ↓
                ORD   LAX

    Step 1: Get a count of incoming edges for each vertex.
        BOS = 0
        JFK = 1
        SFO = 3
        DFW = 3
        MIA = 2
        ORD = 0
        LAX = 2

    Step 2: Add vertices with no incoming edges to ready list.
        ready = [BOS, ORD]

    Step 3: Pop vertex from ready and add to topological sorting list.
        ready = [BOS]
        topo  = [ORD]

    Step 4: Remove outgoing edges from removed vertex and update adjacent
            vertices incoming edge count.  Add to ready list if zero edges.
        DFW = 3-1 = 2

    Step 5: Repeat steps 2 through 4 until ready list is empty.
        a.  ready = []
            topo  = [ORD, BOS]
            SFO = 2, JFK = 0, MIA = 1
            ready = [JFK]

        b.  ready = []
            topo  = [ORD, BOS, JFK]
            DFW = 1, SFO = 1, MIA = 0
            ready = [MIA]

        c.  ready = []
            topo  = [ORD, BOS, JFK, MIA]
            DFW = 0, LAX = 1
            ready = [DFW]

        d.  ready = []
            topo  = [ORD, BOS, JFK, MIA, DFW]
            LAX = 0, SFO = 0
            ready = [LAX, SFO]

        e.  ready = [LAX]
            topo  = [ORD, BOS, JFK, MIA, DFW, SFO]
            ready = [LAX]

        f.  ready = []
            topo  = [ORD, BOS, JFK, MIA, DFW, SFO, LAX]
            ready = []

    The final topological sorting of Figure 14.3d is:

    [ORD, BOS, JFK, MIA, DFW, SFO, LAX]
    """
    return True


def course_prerequisites():
    """Solution to exercise R-14.22.

    Bob loves foreign languages and wants to plan his course schedule for the
    following years. He is interested in the following nine language courses:
    LA15, LA16, LA22, LA31, LA32, LA126, LA127, LA141, and LA169.

    The course prerequisites are:
    • LA15: (none)
    • LA16: LA15
    • LA22: (none)
    • LA31: LA15
    • LA32: LA16, LA31
    • LA126: LA22, LA32
    • LA127: LA16
    • LA141: LA22, LA16
    • LA169: LA32

    In what order can Bob take these courses, respecting the prerequisites?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    This exercise can be solved by performing a topological sorting of a graph
    representing the courses.  The courses are the vertices of the graph, and
    the prerequisites of a course can be viewed as incoming edges.  The courses
    having the following incoming edge counts:

    • LA15: (none)          0
    • LA16: LA15            1
    • LA22: (none)          0
    • LA31: LA15            1
    • LA32: LA16, LA31      2
    • LA126: LA22, LA32     2
    • LA127: LA16           1
    • LA141: LA22, LA16     2
    • LA169: LA32           1

    1.  ready = [LA15, LA22]

    2.  ready = [LA15]
        topo  = [LA22]
        LA126 = 1, LA141 = 1
        ready = [LA15]

    3.  ready = []
        topo  = [LA22, LA15]
        LA16 = 0, LA31 = 0
        ready = [LA16, LA31]

    4.  ready = [LA16]
        topo  = [LA22, LA15, LA31]
        LA32 = 1
        ready = [LA16]

    5.  ready = []
        topo  = [LA22, LA15, LA31, LA16]
        LA32 = 0, LA127 = 0, LA141 = 0
        ready = [LA32, LA127, LA141]

    6.  ready = [LA32, LA127]
        topo  = [LA22, LA15, LA31, LA16, LA141]
        LA126 = 1, LA169 = 1  (Last vertices left)
        ready = [LA32, LA127]

    7.  ready = [LA32]
        topo  = [LA22, LA15, LA31, LA16, LA141, LA127]
        LA126 = 1, LA169 = 1  (Last vertices left)
        ready = [LA32]

    8.  ready = []
        topo  = [LA22, LA15, LA31, LA16, LA141, LA127, LA32]
        LA126 = 0, LA169 = 0
        ready = [LA126, LA169]

    9.  ready = [LA126]
        topo  = [LA22, LA15, LA31, LA16, LA141, LA127, LA32, LA169]
        ready = [LA126]

    10. ready = []
        topo  = [LA22, LA15, LA31, LA16, LA141, LA127, LA32, LA169, LA126]
        ready = []


    Bob can take the language courses in the following order:
    [LA22, LA15, LA31, LA16, LA141, LA127, LA32, LA169, LA126]
    """
    return True


def draw_djikstra():
    r"""Solution to exercise R-14.23.

    Draw a simple, connected, weighted graph with 8 vertices and 16 edges,
    each with unique edge weights. Identify one vertex as a “start” vertex and
    illustrate a running of Dijkstra’s algorithm on this graph.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A simple graph has no self-loops or parallel edges.  A connected graph has
    a path between any to vertices in the graph.  A simple, connected, weighted
    undirected graph with n = 8 vertices and m = 16 edges is shown below:

                64
            a-------b
            | \   / |       11 = a -- d
         38 |   X   | 27    60 = c -- b
            | /   \ |       42 = c -- d
            c-------d
            | \   / |       20 = c -- f
         49 |   X   | 1     33 = e -- d
            | /   \ |       32 = e -- f
            e-------f
            | \   / |       72 = e -- h
         84 |   X   | 30    46 = g -- f
            | /   \ |
            g-------h
                69

    If we set vertex 'a' as the start vertex, then Djikstra's algorithm
    proceeds as follows:

    1.  For all vertices v in G, assign an initial distance of infinity unless
        v is the source vertex, in which case assign a distance of 0.

        distance = {
                    a: 0,
                    b: inf,
                    c: inf,
                    d: inf,
                    e: inf,
                    f: inf,
                    g: inf,
                    h: inf
        }

        Each vertex is also added to a priority queue PQ where the distance is
        the priority.  I will use the distance dictionary above to represent
        the PQ as well.

    2.  As items are removed from the PQ they are added to a second "cloud"
        dictionary that stores each vertex with its minimum distance from the
        source vertex.  The vertex u with the smallest distance will be removed
        from the PQ, which to start will of course be the start vertex 'a'.

        distance = {                    cloud = {
                    b: inf,                     a: 0,
                    c: inf,
                    d: inf,
                    e: inf,
                    f: inf,
                    g: inf,
                    h: inf
        }                               }

    3.  Next, all adjacent vertices v (or destination vertices for a directed
        graph) of u are examined, and if they are not already in the cloud then
        their weights are "relaxed" or updated:

        Adjacent v not in cloud: b, c, d
        distance[a] == d[a] == 0
        d[b] == d[c] == d[d] == inf

        if d[a] + 64 < d[b]:
            d[b] = d[a] + 64 = 0 + 64 = 64
        if d[a] + 38 < d[c]:
            d[c] = d[a] + 38 = 0 + 38 = 38
        if d[d] + 11 < d[d]:
            d[d] = d[a] + 11 = 0 + 11 = 11

        distance = {                    cloud = {
                        b: 64,                  a: 0,
                        c: 38,
                        d: 11,
                        e: inf,
                        f: inf,
                        g: inf,
                        h: inf
            }                           }

    4.  Steps 2 and 3 repeat until PQ is empty.  Below are the final values
        for the cloud dictionary, which represents the shortest distance to
        each vertex v in G from the start vertex 'a':

        cloud = {
                a: 0,
                b: 38,
                c: 32,
                d: 11,
                e: 44,
                f: 12,
                g: 58,
                h: 42
        }
    """
    return True


def directed_djikstra():
    """Solution to exercise R-14.24.

    Show how to modify the pseudo-code for Dijkstra’s algorithm for the case
    when the graph is directed and we want to compute shortest directed paths
    from the source vertex to all the other vertices.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Only a small change is needed to the for loop to make the pseudo-code work
    for a directed graph.  The original for loop from the text is as follows:

        for each vertex v adjacent to u such that v is in Q do

    Two vertices u and v are said to be adjacent if there is an edge whose end
    vertices are u and v.  Specifying that the vertex v be adjacent to vertex u
    works fine for an undirected graph, because an edge is a symmetric relation
    in an undirected graph and the order (u, v) doesn't matter.

    In a directed graph, relations between vertices are asymmetric and are
    represented by directed edges.  If an edge is directed, its first endpoint
    is its origin and the other is the destination of the edge.  The order of
    u and v matter; (u, v) != (v, u).

    The original pseudo-code will select any vertex v that is adjacent to u.
    Adjacent vertices also include the predecessors of u that have outgoing
    edges to vertex u.  In other words, it includes vertices v that are the
    origin vertices of the edges rather than the destinations.  This reverses
    the proper order of the vertices as defined by the directed edge, and will
    result in invalid weight updates.  We can thus rephrase the for loop to:

        for each vertex v that is a destination of u such that v is in Q do

    It's a bit wordier in pseudo-code, but this will ensure only valid
    destination vertices of u will have their weights "relaxed" or updated.
    """
    return True


def draw_prim_jarnik():
    r"""Solution to exercise R-14.25.

    Draw a simple, connected, undirected, weighted graph with 8 vertices and
    16 edges, each with unique edge weights. Illustrate the execution of the
    Prim-Jarnı́k algorithm for computing the minimum spanning tree of this
    graph.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A simple graph has no self-loops or parallel edges.  A connected graph has
    a path between any to vertices in the graph.  A simple, connected, weighted
    undirected graph with n = 8 vertices and m = 16 edges is shown below:

                64
            a-------b
            | \   / |       11 = a -- d
         38 |   X   | 27    60 = c -- b
            | /   \ |       42 = c -- d
            c-------d
            | \   / |       20 = c -- f
         49 |   X   | 1     33 = e -- d
            | /   \ |       32 = e -- f
            e-------f
            | \   / |       72 = e -- h
         84 |   X   | 30    46 = g -- f
            | /   \ |
            g-------h
                69

    Choosing 'a' as the starting vertex, the Prim-Jarnı́k algorithm proceeds as
    follows:

    1.  For all vertices v in G, assign an initial distance of infinity unless
        v is the source vertex, in which case assign a distance of 0.
        A priority queue PQ is also intialized and contains the distance d[v]
        as the priority and the value None as its element.  The dictionary
        below represents PQ.

        distance = {
                    a: (0, None),
                    b: (inf, None),
                    c: (inf, None),
                    d: (inf, None),
                    e: (inf, None),
                    f: (inf, None),
                    g: (inf, None),
                    h: (inf, None)
        }

        The algorithm will replace the None element with an edge that
        represents the minimum-weight edge (u, v) that will be used to build
        the minimum spanning tree T.  The minimum spanning tree T is
        initialized as an empty tree.

    2.  As items are removed from the PQ they are connected to the tree T using
        the edge e associated with the vertex.  The vertex u with the smallest
        distance will be removed from the PQ, which to start will of course be
        the start vertex 'a'.  The vertex 'a' has a distance of zero, and its
        associated edge is None.  This is fine, because the root of a tree
        does not have a parent node and so an edge is not needed.

        Minimum Spanning Tree T:

                            a

    3.  Next, every vertex that is adjacent to vertex u (and not already in the
        tree T) is examined.  If the weight of the edge (u, v) is less than the
        weight associated with vertex v in the PQ, then the entry of v in the
        PQ is updated to reflect the new weight and edge.

        Adjacent vertices to 'a' not in T: b, c, d
        Weights of edges:
                        w(a, b) = 64
                        w(a, c) = 38
                        w(a, d) = 11

        distance = {
                    a: (0, None),
                    b: (64, (a, b)),
                    c: (38, (a, c)),
                    d: (11, (a, d)),
                    e: (inf, None),
                    f: (inf, None),
                    g: (inf, None),
                    h: (inf, None)
        }

    4.  Steps 2 and 3 repeat until PQ is empty.  Below are the final values
        for the vertices after being removed from PQ and inserted into T.
        Finally, the minimum spanning tree T rooted at 'a' is shown below:

        distance = {
                a: (0, None),
                b: (27, (d, b)),
                c: (20, (f, c)),
                d: (11, (a, d)),
                e: (32, (f, e)),
                f: (1, (d, f)),
                g: (46, (f, g)),
                h: (30, (f, h))
        }

        Minimum Spanning Tree T:

                            a
                            | 11
                            |
                            d
                         ___|___
                    27  /       \  1
                       /         \
                      b           f
                            ______|_______
                         20/  | 32    |   \ 30
                          /   |    46 |    \
                         c    e       g     h
    """
    return True


def draw_kruskal():
    r"""Solution to exercise R-14.26.

    Repeat the previous problem for Kruskal’s algorithm.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A simple graph has no self-loops or parallel edges.  A connected graph has
    a path between any to vertices in the graph.  A simple, connected, weighted
    undirected graph with n = 8 vertices and m = 16 edges is shown below:

                64
            a-------b
            | \   / |       11 = a -- d
         38 |   X   | 27    60 = c -- b
            | /   \ |       42 = c -- d
            c-------d
            | \   / |       20 = c -- f
         49 |   X   | 1     33 = e -- d
            | /   \ |       32 = e -- f
            e-------f
            | \   / |       72 = e -- h
         84 |   X   | 30    46 = g -- f
            | /   \ |
            g-------h
                69

    The Kruskal algorithm proceeds as follows:

    1.  Every vertex v in G is added to its own cluster C(v):

    clusters = {
                a: {a},
                b: {b},
                c: {c},
                d: {d},
                e: {e},
                f: {f},
                g: {g},
                h: {h}
    }

        And a priority queue PQ is intialized with every edge in G, prioritized
        by edge weight:

    pq = {
            (64, (a, b)),
            (38, (a, c)),
            (11, (a, d)),
            (60, (b, c)),
            (27, (b, d)),
            (42, (c, d)),
            (49, (c, e)),
            (20, (c, f)),
            (33, (d, e)),
            (1,  (d, f)),
            (32, (e, f)),
            (84, (e, g)),
            (72, (e, h)),
            (46, (f, g)),
            (30, (f, h)),
            (69, (g, h))
    }

        The minimum spanning tree T is initialized to an empty tree.

    2.  Next, the edge (u, v) with the lowest weight is removed from PQ.
        If C(u) != C(v), then the edge is added to T and the clusters are
        merged together.  The first edge to be removed from PQ will be (d, f):

        Lowest weight:          1
        Lowest-weight Edge:     (d, f)
        Compare clusters:       C(d) != C(f)
        Merge:                  C(d) = {d, f}

        Edge (d, f) is added to T:

                    d
                    | 1
                    |
                    f

        clusters = {
                a: {a},
                b: {b},
                c: {c},
                d: {d, f},
                e: {e},
                g: {g},
                h: {h}
        }

    3.  This process continues while T has fewer than n - 1 edges, which is
        8 - 1 = 7 edges for graph G.  The next edge removed from PQ is (a, d):

        Lowest weight:          11
        Lowest-weight Edge:     (a, d)
        Compare clusters:       C(a) != C(d)
        Merge:                  C(a) = {a, d, f}

        Edge (a, d) is added to T:

                    d
               11  /  \ 1
                  /    \
                 a      f

        clusters = {
                a: {a, d, f},
                b: {b},
                c: {c},
                e: {e},
                g: {g},
                h: {h}
        }


    4.  The final minimum spanning tree T is:

                         d
                  _______|_______
             11  /     27|       \ 1
                /        |        \
               a         b         f
                             ______|_______
                          20/  | 32    |   \ 30
                           /   |    46 |    \
                          c    e       g     h
    """
    return True


def bridge_to_islands():
    r"""Solution to exercise R-14.27.

    There are eight small islands in a lake, and the state wants to build seven
    bridges to connect them so that each island can be reached from any other
    one via one or more bridges. The cost of constructing a bridge is propor-
    tional to its length. The distances between pairs of islands are given in
    the following table.

    Find which bridges to build to minimize the total construction cost.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    This exercise can be solved by representing the cost of each bridge as a
    weighted edge between vertices that represent the islands.  The minimum
    spanning tree of this graph G will provide the minimum total construction
    cost of the project.  I will use Kruskal's algorithm to generate the
    minimum spanning tree T.

    1.  Every vertex v in G is added to its own cluster C(v):

    clusters = {
                1: {1},
                2: {2},
                3: {3},
                4: {4},
                5: {5},
                6: {6},
                7: {7},
                8: {8}
    }

        And a priority queue PQ is intialized with every edge in G, prioritized
        by edge weight:

    pq = {
            (240, (1, 2)),
            (210, (1, 3)),
            (340, (1, 4)),
            (280, (1, 5)),
            (200, (1, 6)),
            (345, (1, 7)),
            (120, (1, 8)),
            (265, (2, 3)),
            (175, (2, 4)),
            (215, (2, 5)),
            (180, (2, 6)),
            (185, (2, 7)),
            (155, (2, 8)),
            (260, (3, 4)),
            (115, (3, 5)),
            (350, (3, 6)),
            (435, (3, 7)),
            (195, (3, 8)),
            (160, (4, 5)),
            (330, (4, 6)),
            (295, (4, 7)),
            (230, (4, 8)),
            (360, (5, 6)),
            (400, (5, 7)),
            (170, (5, 8)),
            (175, (6, 7)),
            (205, (6, 8)),
            (305, (7, 8))
    }

        The minimum spanning tree T is initialized to an empty tree.

    2.  Next, the edge (u, v) with the lowest weight is removed from PQ.
        If C(u) != C(v), then the edge is added to T and the clusters are
        merged together.  The first edge to be removed from PQ will be (3, 5):

        Lowest weight:          115
        Lowest-weight Edge:     (3, 5)
        Compare clusters:       C(3) != C(5)
        Merge:                  C(3) = {3, 5}

        Edge (3, 5) is added to T:

                    3
                    | 115
                    |
                    5

        clusters = {
                    1: {1},
                    2: {2},
                    3: {3, 5},
                    4: {4},
                    6: {6},
                    7: {7},
                    8: {8}
        }

    3.  This process continues while T has fewer than n - 1 edges, which is
        8 - 1 = 7 edges for graph G.  The next edge removed from PQ is (1, 8):

        Lowest weight:          120
        Lowest-weight Edge:     (1, 8)
        Compare clusters:       C(1) != C(8)
        Merge:                  C(1) = {1, 8}

        Edge (1, 8) is added to T:

                    3       1
                    | 115   | 120
                    |       |
                    5       8

        clusters = {
                    1: {1, 8},
                    2: {2},
                    3: {3, 5},
                    4: {4},
                    6: {6},
                    7: {7},
        }

    4.  The final minimum spanning tree T is:

                        8
                     ___|______
                120 /   | 155  \ 170
                   /    |       \
                  1     2        5
                    180 |   115 / \ 160
                        |      /   \
                        6     3     4
                    175 |
                        |
                        7

    The minimum total cost to contruct the bridges is thus $1075.
    """
    return True
