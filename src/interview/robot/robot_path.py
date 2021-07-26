"""Solution to robot path programming test.

###############################################################################
# robot_path.py
#
# Revision:     1.00
# Date:         7/22/2021
# Author:       Alex
#
# Purpose:      Complete the programming exercise detailed below.
#
###############################################################################

You have been e-mailed a few TEXT data files. One is called "Programming Test A
Data File.txt" while another is called "Programming Test A Data File
(Example).txt." These files contain a representation of a map using simple
ASCII text. In this map the characters have the following meaning:

character '#' (a hashtag symbol) represents an obstacle
character '.' (a period) represents open space
character 'R' (a capital R) represents the location of a robot
character 'G' (a capital G) represents a goal location

The map does not ‘wrap,’ i.e., do not assume that moving off the map to the
left brings you to the right side of the map (same for the top and bottom).

Write a program that does the following:

- Reads the provided map in "Programming Test A Data File.txt" into memory.
  Store it in any data structure you find convenient for the following steps.

- Write a function that can print out this map to the screen or to a file
  (whichever is more convenient for your debugging). Verify that the map was
  read in correctly.

- Write an algorithm to find the shortest path from the robot location ('R') to
  the goal location ('G').

- Modify the function that prints out the map to also print out the path of the
  robot.  It should write to the screen or a file. The path the robot will take
  should be represented as 'O' (capital letter O) characters. The file
  "Programming Test A Data File (Example).txt" provides an example of such a
  path printed out to a file.

After completing steps 1-4, time permitting, you can try a few other map files
to test your algorithm.

-------------------------------------------------------------------------------
Solution:
-------------------------------------------------------------------------------
The steps to the solution of this problem are as follows:

1.  Read in the ASCII map
2.  Assign the characters of the map to vertices in a weighted graph G
3.  Run Djikstra's algorithm on G for the vertex containing the robot
4.  Compute the shortest-path tree from the resulting distance map
5.  Modify the ASCII map to show the robot's path to the goal and write to disk

The solution will require writing classes to implement the following:
1. A Graph class implemented using an adjacency map
    a. A nested Vertex class for the Graph
    b. A nested Edge class for the Graph
    c. A Map class implemented using a hash table for the adjacency map
    d. A nested Item class for the Map
2. An AdaptablePriorityQueue class implemented using a heap
    a. A nested Item class for the AdaptablePriorityQueue
    b. A Heap class
    c. A BinaryTree class to implement the Heap class
    d. A nested Node class for the BinaryTree
    e. A circular queue to implement BFS for the binary tree

The solution will require writing functions to implement the following:
1. Reading in the ASCII map and converting it into a graph
2. Djikstra's algorithm to compute shortest distances to each vertex
3. Computing the shortest-path tree for each vertex (other than start)
4. Converting the shortest-path tree to the goal to ASCII coordinates
5. Modifying the ASCII map to show the shortest path and writing it to disk
"""

# %% Imports
# Standard system imports
from pathlib import Path
import os

# Related third party imports
import numpy as np

# Local application/library specific imports
from interview.robot.graph_data_structures import Graph
from interview.robot.array_data_structures import Map
from interview.robot.heap_data_structures import AdaptablePriorityQueue


# %% Solution
def map_to_graph(filename):
    """Read in ASCII map and return a graph representation of the map.

    Also return starting vertex of robot and goal vertex.  Return a map with
    vertex keys to (row, column) tuples of the vertex coordinates in the map.
    """
    arr = np.loadtxt(filename, dtype=object, comments=None, delimiter='\n')
    nrows = len(arr)                            # Number rows in map
    ncols = len(arr[0])                         # Number columns in map
    g = Graph()                                 # Undirected graph
    vert_arr = np.empty(shape=(nrows, ncols), dtype=object)
    vert_map = Map()                            # Map each vert to its coord
    for row in range(nrows):                    # Add vertices to graph
        for col in range(ncols):                # And to vertex array
            vertex = g.insert_vertex(arr[row][col])
            vert_arr[row, col] = vertex
            if arr[row][col] == 'R':
                robot = vertex                  # Start vertex of robot
            elif arr[row][col] == 'G':
                goal = vertex                   # Goal vertex
            vert_map[vertex] = (row, col)       # Map vertex to coordinates
    for row in range(nrows):
        for col in range(ncols):
            add_edges(row, col, g, vert_arr)    # Add weighted edges to graph
    return g, robot, goal, vert_map


def add_edges(row, col, g, vert_arr):
    """Add weighted edges between adjacent vertices.

    Do not add an edge if it already exists.
    """

    def insert_edge(u, v, g):
        """Add edge of appropriate weight if edge does not exist."""
        if g.get_edge(u, v) is None:
            if u.element() == '#' or v.element() == '#':
                weight = np.inf     # Obstacle
            else:
                weight = 1          # Open space, robot, goal
            g.insert_edge(u, v, weight)

    nrows = len(vert_arr)                       # Number rows in map
    ncols = len(vert_arr[0])                    # Number columns in map
    u = vert_arr[row, col]                      # Current vertex in map
    if row > 0:
        v = vert_arr[row-1, col]                # Vertex above u
        insert_edge(u, v, g)
    if row < nrows-1:
        v = vert_arr[row+1, col]                # Vertex below u
        insert_edge(u, v, g)
    if col > 0:
        v = vert_arr[row, col-1]                # Vertex left of u
        insert_edge(u, v, g)
    if col < ncols-1:
        v = vert_arr[row, col+1]                # Vertex right of u
        insert_edge(u, v, g)


def shortest_path_length(graph, start):
    """Calculate the length of the shortest path using Djikstra's algorithm."""
    dist = Map()                        # Distance map
    queue = AdaptablePriorityQueue()    # Priority queue with distance keys
    cloud = Map()                       # Keep track of relaxed vertices
    pqlocator = Map()                   # Keep track of vertices in queue
    for vertex in graph.vertices():     # Initialize distances of vertices
        if vertex is start:
            dist[vertex] = 0            # Start vertex 0 distance to itself
        else:
            dist[vertex] = np.inf       # Infinite distance for all other verts
        pqlocator[vertex] = queue.enqueue(dist[vertex], vertex)
    while not queue.is_empty():
        min_dist, u = queue.dequeue()
        cloud[u] = min_dist             # Add vertex to cloud with minimum dist
        for edge in graph.incident_edges(u):
            vertex = edge.opposite(u)
            if cloud.get(vertex, None) is None:  # Vertex is in queue
                weight = graph.get_edge(u, vertex).element()
                if dist[u] + weight < dist[vertex]:
                    dist[vertex] = dist[u] + weight  # Relaxation step
                    queue.update(pqlocator[vertex], dist[vertex], vertex)
    return cloud


def shortest_path_tree(graph, start, cloud):
    """Compute the shortest-path tree rooted at start vertex.

    Return tree as a map of vertices v (excluding start) to edges e=(u, v).
    The vertex u is the preceding node along the shortest path to v.

    The edge is specified as an incoming edge in the case of a directed graph.
    The cloud map from Djikstra's algorithm is used to determine the shortest
    path from the start vertex to every other vertex.
    """
    tree = Map()                         # Map vertices to parent edges
    for vertex, _ in cloud:
        if vertex is not start:
            for edge in graph.incident_edges(vertex, out=False):
                u = edge.opposite(vertex)
                weight = edge.element()
                if cloud[vertex] == cloud[u] + weight:
                    tree[vertex] = edge  # Edge along shortest path to vertex
    return tree


def calculate_shortest_path_coords(start, goal, tree, vert_map):
    """Iterate through edges backwards from goal to start.

    Return a list of tuples representing the (row, column) position of the
    characters in the ASCII map along the shortest path.
    """
    coords = []
    vertex = tree[goal].opposite(goal)  # Vertex directly preceding goal
    while vertex is not start:
        coord = vert_map[vertex]  # (row, column) tuple of vertex in ASCII map
        coords.append(coord)
        edge = tree[vertex]             # Edge along shortest path to vertex
        vertex = edge.opposite(vertex)  # Next vertex going backwards to start
    return coords


def write_map(filename, coords):
    """Iterate through shortest path coordinates and write ASCII path.

    Read in ASCII map and mark the shortest path with 'O' characters.
    Write the modified ASCII to a new file appended with _SOLUTION.

    Return the filename of the file written to disk.
    """
    out_fn = filename.parent / (filename.stem + '_SOLUTION.txt')
    arr = np.loadtxt(filename, dtype=object, comments=None, delimiter='\n')
    for coord in coords:
        row, col = coord
        str_list = list(arr[row])
        str_list[col] = 'O'     # Mark robot's path with 'O'
        arr[row] = ''.join(str_list)
    # Annoying hack to remove the final newline created by np.savetxt()
    with open(out_fn, 'w') as fout:
        newline_size_in_bytes = len(os.linesep)
        np.savetxt(fout, arr, fmt="%s")  # Use np.savetxt.
        fout.seek(0, os.SEEK_END)  # Go to the end of the file.
        # Go backwards appropriate number of bytes from the end of the file.
        fout.seek(fout.tell() - newline_size_in_bytes, os.SEEK_SET)
        fout.truncate()  # Truncate the file to this point.
    return out_fn


def robot_solution(filename):
    """Solution to shortest path from the robot location to goal location.

    Return filename of solution file written to disk.
    """
    filename = Path(filename)  # Ensure filename is a Path object
    # Read in ASCII map and return graph representation
    graph, start, goal, vert_map = map_to_graph(filename)
    # Run Djikstra's algorithm to calculate the shortest path length
    cloud = shortest_path_length(graph, start)
    if cloud[goal] == np.inf:   # Check if goal is reachable
        print('\nGoal is unreachable from start!\n')
        # Write unmodified ASCII map to disk as solution
        out_fn = write_map(filename, [])
    else:
        print(f'\nThe shortest path to the goal is: {cloud[goal]}\n')
        # Calculate tree representing shortest path to goal
        tree = shortest_path_tree(graph, start, cloud)
        # Calculate the coordinates in the ASCII map of the shortest path
        coords = calculate_shortest_path_coords(start, goal, tree, vert_map)
        # Write an ASCII map to disk showing the shortest path
        out_fn = write_map(filename, coords)
    print('File written to:')
    print(f'{out_fn}\n')
    return out_fn
