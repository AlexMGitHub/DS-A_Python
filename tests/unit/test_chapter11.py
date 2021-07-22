#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 11 exercises.

###############################################################################
# test_chapter11.py
#
# Revision:     1.00
# Date:         7/9/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 11 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports
import pytest
import numpy as np

# Local application/library specific imports
import dsa.chapter11_exercises as chap11


# %% Reinforcement Exercises
def test_bst_insertions():
    """Solution to exercise R-11.1.

    If we insert the entries (1, A), (2, B), (3,C), (4, D), and (5, E),
    in this order, into an initially empty binary search tree, what will it
    look like?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The items in a binary search tree must be stored according to the following
    rules.  For a position p storing a key-value pair (k,v):
    1. Keys stored in the left subtree of p are less than k
    2. Keys stored in the right subtree of p are greater than k

    The resulting subtree looks as follows:

    (1, A)
        (2, B)
            (3, C)
                (4, D)
                    (5, E)

    Note that (1, A) is the root of the tree, and each subsequent item is the
    right child of its parent.  The keys are inserted in ascending order of
    value, and so the height of the tree is equal to n, the number of items.
    This is the worst-case scenario for a binary search tree.
    """
    assert chap11.bst_insertions()


def test_draw_bst_insertions():
    """Solution to exercise R-11.2.

    Insert, into an empty binary search tree, entries with keys 30, 40, 24, 58,
    48, 26, 11, 13 (in this order). Draw the tree after each insertion.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    1.
    30

    2.
    30
        40

    3.
        30
    24      40

    4.
        30
    24      40
                58

    5.
        30
    24      40
         48    58

    6.
         30
    24        40
       26  48    58

    7.
            30
       24       40
    11   26  48    58

    8.
            30
       24       40
    11   26  48    58
      13
    """
    assert chap11.draw_bst_insertions()


def test_how_many_bst():
    """Solution to exercise R-11.3.

    How many different binary search trees can store the keys {1, 2, 3}?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The order of the nodes in a binary search tree depends on the order of
    key insertions.  There are 3! = 6 permutations of the keys {1, 2, 3}, which
    generates 6 different key insertion orders.  However, not all of the
    resuling binary search trees will be unique:

    1. {1, 2, 3}
        1
          2
            3

    2. {1, 3, 2}
        1
          3
        2

    3. {2, 1, 3}
        2
      1   3

    4. {2, 3, 1}
        2
      1   3

    5. {3, 1, 2}
        3
      1
        2

    6. {3, 2, 1}
        3
      2
    1

    Trees 3 and 4 are identical, and so there are five unique (different)
    binary search trees.
    """
    assert chap11.how_many_bst()


def test_nonrecursive_search():
    """Solution to exercise R-11.6.

    Our implementation of the TreeMap._subtree search utility, from Code
    Fragment 11.4, relies on recursion. For a large unbalanced tree, Python’s
    default limit on recursive depth may be prohibitive. Give an alternative
    implementation of that method that does not rely on the use of recursion.
    """
    tm_orig = chap11.TreeMap()
    tm_new = chap11.TreeMapNonRecursiveSearch()
    n = 100             # Length of sequence of random integers
    low = 500           # Lower boundary of random integer range
    high = 1000         # Upper boundary of random integer range
    rng = np.random.default_rng(37)
    rints = tuple(rng.choice(range(low, high+1), size=n, replace=False))
    for x in rints:     # Add some key-value pairs to the tree maps
        tm_orig[x] = x
        tm_new[x] = x
    for x in rints:
        assert tm_orig[x] == tm_new[x]  # Verify get operation works
    with pytest.raises(KeyError):
        tm_new[low-1]                   # Key does not exist
    with pytest.raises(KeyError):
        tm_new[high+1]                  # Key does not exist
    for count, x in enumerate(rints):
        del tm_orig[x]                  # Delete item
        del tm_new[x]
        if count > n//2:
            break                       # Only delete half of items
    for orig, new in zip(tm_orig, tm_new):
        assert orig == new              # Verify that items match original


def test_trinode_restructurings():
    """Solution to exercise R-11.7.

    Do the trinode restructurings in Figures 11.12 and 11.14 result in single
    or double rotations?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    1. A double rotation occurs when position x has the middle of the three
    relevant keys; otherwise it is a single rotation.

    2. Position x is the position to be rotated, position y is x's parent, and
    position z (if it exists) is x's grandparent (y's parent).

    3. Positions (a, b, c) are a left-to-right inorder listing of the positions
    x, y, and z.

    Figure 11.12 shows a trinode restructuring after the insertion of a new
    element into the tree at position p.  Position z is defined as the first
    position encountered when moving up the tree from p such that z is
    unbalanced (height of children differs by more than 1).  Position y is then
    the child of z with higher height that is also an ancestor of p.  Position
    x is the child of y with higher height that is also an ancestor of p (and
    could be p itself).  In figure 11.12, x's key has value 62, y is 50, and
    z is 78.  Position x will also be labeled as position b as it is the second
    position visited inorder.  We know from (1) above that if x is the middle
    of three keys there will be a double rotation.  Position x will first be
    rotated with y, and then rotated again with z.

    Figure 11.14 shows a trinode restructuring after the deletion of an element
    in the tree.  In this case, position p represents the parent of the deleted
    element.  Position z is again defined as the first position encountered
    when moving up the tree from p such that z is unbalanced.  Position y is
    the child of z with higher height, but in this case y is *not* an ancestor
    of p.  Position x is the child of y with higher height, or if the heights
    are equal, the child on the same side of y as the side y is on z.  In this
    case y's children have equal heights, and so x is chosen as the right child
    of y as y is the right child of z.  In figure 11.14, x's key has a value of
    78, y is 62, and z is 44.  Position x is the largest of the three keys, and
    so from (1) we know that there will be a single rotation.  Position y is
    rotated with position z, and the resulting node configuration is balanced.
    """
    assert chap11.trinode_restructurings()


def test_draw_avl_insertion():
    """Solution to exercise R-11.8.

    Draw the AVL tree resulting from the insertion of an entry with key 52
    into the AVL tree of Figure 11.14b.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    They key of 52 would become the left child of the element with key 54.
    Once added, position z, the first unbalanced position when moving up the
    tree, is 44.  Its left child has height 1, and its right child now has
    height 3.  This right child, 50, becomes position y.  Position x is key 54,
    as it is the child of y with the highest height and an ancestor of p.
    We can immediately tell that the trinode restructuring will be a single
    rotation, as x has the highest key value.  Position y (key 50) will rotate
    with position z (key 44).  The resulting tree will look like below:

    Before restructuring:
                    62
            44              78
        17      50                88
            48      54
                 52

    After restructuring:
                    62
            50              78
        44      54                88
      17  48  52

    The nodes are all balanced, as can be seen when representing the nodes with
    their heights rather than their keys (empty subtrees have height 0):

                    4
            3               2
        2       2        0      1
      1   1   1   0           0   0

    The heights of the children of all nodes differ by no more than 1.
    In addition, the children of the resulting tree all obey the requirements
    that the keys of left children are smaller then their parent, and the keys
    of right children are larger than their parent.  Finally, an inorder
    traversal of the tree returns the keys in increasing order:

    17, 44, 48, 50, 52, 54, 62, 78, 88
    """
    assert chap11.draw_avl_insertion()


def test_draw_avl_deletion():
    """Solution to exercise R-11.9.

    Draw the AVL tree resulting from the removal of the entry with key 62
    from the AVL tree of Figure 11.14b.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Key 62 is the root of the tree in Figure 11.14b.  In addition, it has two
    children, which means that we must perform the following procedure:

    1. Locate position r = before(p), the greatest key that is strictly less
       than position p.  It is the right-most position of the left subtree of
       the deleted position p.  In Figure 11.14b this is the position that
       contains key 54.

    2. Position r's item is moved to the root as a replacement for the deleted
       key of 62.  That is, key 54 is moved to the root.

    3. Position r is deleted from the tree.

    Before deletion:
                    62
            44              78
        17      50                88
             48    54

    After deletion:
                    54
            44              78
        17      50                88
             48

    Deleting a node from an AVL tree in general requires restructuring.  The
    positions x, y, z are derived from the *parent node* of the deleted
    position.  In this case, the deleted node was the root of the tree and
    has no parent.  However, the AVL tree doesn't require restructuring as the
    tree is balanced.  The tree's nodes are represented with their heights:

                     4
             3              2
         1      2        0       1
             1    0

    The heights of the children of each node do not differ by more than 1.
    Finally, an inorder traversal of the tree returns the keys in increasing
    order:

    17, 44, 48, 50, 54, 78, 88
    """
    assert chap11.draw_avl_deletion()


def test_array_rotation():
    """Solution to exercise R-11.10.

    Explain why performing a rotation in an n-node binary tree when using
    the array-based representation of Section 8.3.2 takes Ω(n) time.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    In an array-based binary tree, every position p in the tree is represented
    according to a function f(p).  The function f(p) performs level numbering,
    where the array index of a node is determined by its level in the tree and
    its position from left to right.  If a node changes positions in the tree,
    its level number must be updated and the node must be moved to the
    corresponding index in the array.

    A rotation swaps the positions of two nodes (x and y) and changes their
    level numbering.  But the rotation will also change the level numbering of
    every node contained in the 3 subtrees rooted at the children of x and y.
    This is because two of the three subtrees will change levels, which changes
    their level numbering.  The middle subtree will not change levels, but it
    will shift either left or right in the tree and thus also require
    renumbering.

    Although it's true that this renumbering will only affect the rotated nodes
    and their subtrees, in general the number of nodes affected by a rotation
    is proportional to n.  As n grows and the tree increases in size the
    expected number of nodes affected by a rotation grows as well.
    Even if we assume that each node's renumbering and swapping operation is
    O(1), the rotation operation's lower bound must be linear in n.  As an
    example, a rotation involving the root of the tree will cause all n nodes
    in the tree to be renumbered.  A rotation at a deeper depth in the tree
    will still cause some fraction of n nodes to be renumbered.

    In other words, a rotation operation on an array-based representation of a
    binary tree is Ω(n).
    """
    assert chap11.array_rotation()


def test_splay_tree_ops():
    """Solution to exercise R-11.14.

    Perform the following sequence of operations in an initially empty splay
    tree and draw the tree after each set of operations.
    a. Insert keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.
    b. Search for keys 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, in this order.
    c. Delete keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    a. Because the insertions in (a) are made in increasing order of key value,
       only zigs will be performed to create the resulting splay tree:

    Result after a:
             18
            16
           14
          12
         10
        8
       6
      4
     2
    0

    b. All of the key searches in (b) are unsuccessful and terminate at the
       right child of each node in the tree in increasing order.

    Result after b:
            18
           16
          14
         12
        10
       8
      6
     4
    0
     2

    c. After deleting all of the keys the tree is empty.
    """
    assert chap11.splay_tree_ops()


def test_splay_tree_access_keys():
    """Solution to exercise R-11.15.

    What does a splay tree look like if its entries are accessed in increasing
    order by their keys?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A splay operation moves the accessed node to the root of the tree.
    First, the smallest key will be moved the root.  Next, the second-smallest
    key will move to the root, and the smallest key will have to be assigned
    as its left child to maintain an inorder relationship.  When the third-
    smallest key is splayed to the root, the second-smallest key and its left
    subtree containing the smallest key will also become the left child of the
    new root.

    Accessing each entry in order will thus create a tree of height n-1, where
    every node is the left child of its parent.  The largest key will be
    accessed last and moved to the root of the tree, having height n-1.  The
    smallest key will have depth n-1, and every key will have height ordered
    by increasing key value.
    """
    assert chap11.splay_tree_access_keys()


def test_tree_2_4_or_not():
    """Solution to exercise R-11.16.

    Is the search tree of Figure 11.23(a) a (2, 4) tree? Why or why not?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A (2, 4) tree must meet the following criteria:
    1. Size property: Every internal node has at most four children
    2. Depth property: All the external nodes have the same depth

    The tree in Figure 11.23(a) obeys (1), but violates (2).  Some of the
    external nodes have a depth of 3, and others have a depth of 4.  Therefore
    Figure 11.23(a) is not a (2, 4) tree.
    """
    assert chap11.tree_2_4_or_not()


def test_alternative_split():
    r"""Solution to exercise R-11.17.

    An alternative way of performing a split at a node w in a (2, 4) tree is
    to partition w into w' and w" , with w' being a 2-node and w" a 3-node.
    Which of the keys k_1 , k_2 , k_3 , or k_4 do we store at w’s parent? Why?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Key k_2 must be stored at w's parent.  Take Figure 11.26 for example, where
    key k_4 (17) has just been inserted into node w:

    (5 10 12)
            \
            (13 14 15 17)
            /  /  |  \  \

    The w node is (13 14 15 17) which has overflowed because it now has 5
    children.  The u node (w's parent) is (5 10 12).  w' will be (13) with two
    children, making it a 2-node storing k_1.  w" will be (15 17) with three
    children, making it a 3-node storing keys k_3 and k_4.  k_2 (key 14) will
    be stored in node u:

    (5 10 12 14)
            /   \
        (13)  (15 17)
        /  \  /  |  \

    k_2 is the only key that is greater than the 2-node containing key k_1, but
    also less than the 3-node containing keys k_3 and k_4.  Therefore it must
    be stored in node u.  Note that now the u node has overflowed.  The
    splitting will continue up the tree until the nodes all meet the (2, 4)
    properties.
    """
    assert chap11.alternative_split()


def test_draw_2_4_tree():
    r"""Solution to exercise R-11.20.

    Consider the set of keys K = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15}.
    a. Draw a (2, 4) tree storing K as its keys using the fewest number of
       nodes.
    b. Draw a (2, 4) tree storing K as its keys using the maximum number
       of nodes.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    a.  Fewest nodes
    I assume that fewest number of nodes includes both internal and external
    nodes.  In order to minimize the number of nodes, each node should have the
    maximum number of keys.  This is 3 keys per node for a (2, 4) tree as a
    node with 3 keys has four children.  There are 15 keys in the list, and so
    this would evenly divide into 5 nodes of 3 children.  However, the nodes
    must also be arranged such that all external nodes have the same depth.

                (4 8 12)
          /       | |        \
    (1 2 3) (5 6 7) (9 10 11) (13 14 15)
    / | | \ / | | \  / | | \   / | | \

    The above configuration results in 5 internal nodes and 16 external nodes,
    for a total of 21 nodes.

    b. Maximum nodes
    The maximum number of nodes occurs when every node contains no more than
    1 key.  Again, all external nodes must have the same depth.

                    8
            4               12
        2       6       10      14
      1   3   5   7   9   11  13  15
     / \ / \ / \ / \ / \  / \ / \ / \

    The above configuration has 15 internal nodes and 16 external nodes for a
    total of 31 nodes.
    """
    assert chap11.draw_2_4_tree()


def test_draw_2_4_red_black_trees():
    r"""Solution to exercise R-11.21.

    Consider the sequence of keys (5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1).
    Draw the result of inserting entries with these keys (in the given order)
    into:
    a. An initially empty (2, 4) tree.
    b. An initially empty red-black tree.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    a. (2, 4) tree:

              (10 22)
          /      |     \
    (1 2 5) (12 16 18) (30 45 50)

    b. Red-black tree:

                    B22
                /           \
            R10             B45
          /    \           /  \
        B2      B16      R30  R50
       /  \     /  \
      R1  R3  R12  R18

    Per the red-black tree rules:
    1. The root is black
    2. The children of a red node are black
    3. All nodes with zero or one children have the same number of black
       ancestors (in this case, 2 ancestors)
    """
    assert chap11.draw_2_4_red_black_trees()


def test_red_black_true_false():
    r"""Solution to exercise R-11.22.

    For the following statements about red-black trees, provide a justification
    for each true statement and a counterexample for each false one.

    a. A subtree of a red-black tree is itself a red-black tree.
    b. A node that does not have a sibling is red.
    c. There is a unique (2, 4) tree associated with a given red-black tree.
    d. There is a unique red-black tree associated with a given (2, 4) tree.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    a. False.  A red-black tree's root must be black, and a subtree of a red-
       black tree could be rooted at a red node.

    b. False.  The root does not have a sibling node, and the root must be
       black.

    c. True.  Figure 11.32 shows that any legal configuration of red-black
       nodes has a single equivalent representation as a (2, 4) tree.

    d. False.  If node w is a 3-node (x y), it can be represented as either:
        Bx                  By
       /  \        or      /  \
           Ry            Rx

       And so there is not a unique red-black tree associated with a given
       (2, 4) tree.
    """
    assert chap11.red_black_true_false()


def test_inorder_listing():
    """Solution to exercise R-11.23.

    Explain why you would get the same output in an inorder listing of the
    entries in a binary search tree, T, independent of whether T is maintained
    to be an AVL tree, splay tree, or red-black tree.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    All binary search trees store a set S of unique elements in nodes according
    to the following properties:

    1. Position p stores an element of S, denoted as e(p)
    2. Elements stored in the left subtree of p are less than e(p)
    3. Elements stored in the right subtree of p are greater than e(p)

    These properties assure that an inorder traversal of a binary search tree
    T visits the elements in nondecreasing order.  Therefore, regardless of the
    particular type of binary search tree the inorder listing of the entries
    will be identical.
    """
    assert chap11.inorder_listing()


def test_worst_case_height():
    """Solution to exercise R-11.24.

    Consider a tree T storing 100,000 entries. What is the worst-case height
    of T in the following cases?

    a. T is a binary search tree.
    b. T is an AVL tree.
    c. T is a splay tree.
    d. T is a (2, 4) tree.
    e. T is a red-black tree.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    a. The worst-case height for a BST is n, so a height of 100,000.
    b. The worst-case height of an AVL tree is 2*logn + 2, so a height of 36.
    c. The worst-case height of a splay tree is n, so a height of 100,000.
    d. The worst-case height of a (2, 4) tree is log(n+1), so a height of 17.
    e. The worst-case height of a red-black tree is 2*log(n+1)-2, height of 32.
    """
    assert chap11.worst_case_height()


if __name__ == '__main__':
    test_nonrecursive_search()
