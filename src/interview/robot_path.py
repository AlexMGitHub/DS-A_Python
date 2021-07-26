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
2. An  AdaptablePriorityQueue class implemented using a heap
    a. A nested Item class for the AdaptablePriorityQueue
    b. A BinaryTree class to implement the heap
    c. A nested Node class for the BinaryTree
    d. A circular queue to implement BFS for the binary tree

The solution will require writing functions to implement the following:
1. Reading in the ASCII map and converting it into a graph
2. Djikstra's algorithm
3. Computing the shortest-path tree
4. Converting the shortest-path tree to an ASCII map
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
