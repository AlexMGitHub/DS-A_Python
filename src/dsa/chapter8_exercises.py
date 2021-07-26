#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 8 exercises.

###############################################################################
# chapter8_exercises.py
#
# Revision:     1.00
# Date:         7/05/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 8 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
from textbook_src.ch08.linked_binary_tree import LinkedBinaryTree
from textbook_src.ch08.euler_tour import BinaryEulerTour


# %% Reinforcement Exercises
def figure_8p3():
    """Solution to exercise R-8.1.

    The following questions refer to the tree of Figure 8.3.
    a. Which node is the root?
    b. What are the internal nodes?
    c. How many descendants does node cs016/ have?
    d. How many ancestors does node cs016/ have?
    e. What are the siblings of node homeworks/?
    f. Which nodes are in the subtree rooted at node projects/?
    g. What is the depth of node papers/?
    h. What is the height of the tree?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    a. /user/rt/courses/
    b. /user/rt/courses/, cs016/, cs252/, homeworks/, programs/, projects/,
       papers/, demos/
    c. Including itself, it has 10 descendants
    d. Including itself, it has 2 ancestors
    e. grades and programs/
    f. projects/, papers/, demos/, buylow, sellhigh, market
    g. 3
    h. 4
    """
    return True


def worst_case_depth():
    """Solution to exercise R-8.2.

    Show a tree achieving the worst-case running time for algorithm depth.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    From the text, depth's worst-case run time is O(n) when all nodes form a
    single branch of depth n-1.  For n = 4:

    root_node       (depth 0)
    |
    node1           (depth 1)
    |
    node2           (depth 2)
    |
    node3           (depth 3, or n-1)
    """
    return True


def justify_prop_8p4():
    """Solution to exercise R-8.3.

    Give a justification of Proposition 8.4.

    Proposition 8.4: The height of a nonempty tree T is equal to the maximum of
    the depths of its leaf positions.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. All nodes are descendants of the root node, meaning that there is a path
       from the root node to every other node in the tree.
    2. Height is defined recursively as:
       a. If p is a leaf, height = 0
       b. Otherwise, height = max( height(children_of_p) )
    3. The depth of p is the number of its ancestors, excluding itself

    Therefore:
    1. The leaf with the maximum depth has the most ancestors of any node
    2. The root will be the top-most ancestor of any node in the tree
    3. The height of the root node will thus be equal to the height of the tree
    4. The depth of path from root to max depth leaf is equal to the height of
       the root node
    5. Therefore the height of a non-empty tree is equal to the maximum of the
       depths of its leaf positions.
    """
    return True


def runnng_time_of_height():
    """Solution to exercise R-8.4.

    What is the running time of a call to T.height2(p) when called on a
    position p distinct from the root of T? (See Code Fragment 8.5.)

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    From the text, height2() spends O(c_p + 1) time at each position p
    computing the maximum of the height of p's children.  The variable c_p
    represents the number of children of node p.  The overall running time per
    the text is O( sum_p(c_p + 1) ).

    If p is the root of the tree, this simplifies to O(n + n-1) = O(n).
    We can split the summation into two summations to see why this is:

    O( sum_p(1) + sum_p(c_p) )

    The left sum is counting all nodes p in the tree T, which is equal to n.
    The right sum is counting the number of children in the tree, which is
    equal to n-1 as the root node is not a child of any other node.

    This exercise asks for the running time of a node in T that is not the root
    node.  This means that height2() will run over a subtree rooted at some
    position p that is not the root of T.  If this subtree has m nodes, then
    all of the above logic applies to the subtree of T rooted at p:

    = O( sum_p(1) + sum_p(c_p) )

    = O(m + m-1)

    = O(2m-1)

    = O(m)

    The running time of a call to T.height2(p) when called on a position p
    that is the root of a subtree with m nodes is O(m).
    """
    return True


def count_left_children():
    """Solution to exercise R-8.5.

    Describe an algorithm, relying only on the BinaryTree operations, that
    counts the number of leaves in a binary tree that are the left child of
    their respective parent.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The following solution uses three methods from the BinaryTree class:
        -   inorder():  Generator to traverse tree and return all positions p
        -   is_leaf(p): Inherited method from Tree class, True if node is leaf
        -   left(p):    Abstract method returns left child of p


    def count_left_children(self):
        count = 0
        for p in self.inorder():
            if self.is_leaf(p) and p == self.left(parent):
                count += 1
        return count


    My solution traverses the entire tree and returns every position in it.
    The counter is only incremented if the position represents a leaf node
    that is the left child of its parent node.
    """
    return True


def improper_binary_tree():
    r"""Solution to exercise R-8.7.

    What are the minimum and maximum number of internal and external
    nodes in an improper binary tree with n nodes?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A binary tree is proper if if each node has either zero or two children.
    All internal nodes in a proper binary tree have 2 children.  An improper
    binary tree thus has internal nodes that do not have 2 children.
    I assume that an improper binary tree still adheres to the other properties
    of a binary tree, such as having a maximum of 2 children.

    A proper binary tree T with n_E external nodes and n_I internal nodes has
    n_E = n_I + 1.  We also know that n = n_E + n_I must hold true for any
    binary tree, proper or improper.

    An improper tree must have at least one internal node with 1 child.  If an
    internal node has 0 children then it is an external node.  If we minimize
    the number of internal nodes for a tree T with a fixed number of nodes n,
    then we maximize the number of external nodes.  The reverse is also true.

    To maximize the number of internal nodes, we restrict each node to having
    at most 1 child, and there will be only 1 external node.  This will
    resemble a long line of nodes.  An example is shown for n = 7:

    n = 7
    n_E = 1
    n_I = n - 1 = 7 - 1 = 6

                                1
                                |
                                2
                                |
                                3
                                |
                                4
                                |
                                5
                                |
                                6
                                |
                                7

    To maximize the number of external nodes, we want a tree that is as close
    to a proper binary tree as possible.  A proper binary tree will always have
    more external nodes than an improper tree for the same number of n nodes,
    because a proper tree can have 2 leaves per internal node, while an
    improper tree must have at least one of these internal nodes contain only a
    single leaf.

    In other words, we want a proper binary tree that has one internal node
    that is improper to maximize the number of external nodes.  That is only
    possible if n is a power of 2.  If n is not a power of 2, every external
    node added to the tree turns an existing leaf node into an internal node.
    This means that the external node count will not increase until enough
    nodes have been added to reach the next power of 2.

    The formulas to maximize the number of external nodes in an improper tree
    are thus as follows:

    if n is a power of 2:
        n_E = n_I = n / 2
    else:
        n_E = ceil(log(n))
        n_I = n - n_E

    Examples are shown for n = 4, 5, 6, 7, 8, and 9:

    n = 4                                           1
    n_E = n_I = 2                                 /   \
    n_I = 2                                      2     3
                                                / \
                                               4

    n = 5                                           1
    n_E = ceil(log(5)) = 3                        /   \
    n_I = 2                                      2     3
                                                / \
                                               4   5

    n = 6                                           1
    n_E = ceil(log(6)) = 3                        /   \
    n_I = 3                                      2     3
                                                / \   / \
                                               4   5 6

    n = 7                                           1
    n_E = ceil(log(7)) = 3                        /   \
    n_I = 4                                      2     3
                                                / \   / \
                                               4   5 6
                                              / \
                                             7

    n = 8                                           1
    n_E = n_I = 4                                 /   \
    n_I = 4                                      2     3
                                                / \   / \
                                               4   5 6   8
                                              / \
                                             7

    n = 9                                           1
    n_E = ceil(log(9)) = 4                        /   \
    n_I = 5                                      2     3
                                                / \   / \
                                               4   5 6   8
                                              / \       / \
                                             7         9


    The minimum and maximum number of internal and external nodes in an
    improper binary tree with n nodes are:

    Minimum internal nodes, maximum external nodes:
    if n is a power of 2:
        n_E = n_I = n / 2
    else:
        n_E = ceil(log(n))
        n_I = n - n_E

    Maximum internal nodes, minimum external nodes:
    n_I = n - 1
    n_E = 1
    """
    return True


def draw_aet():
    r"""Solution to exercise R-8.13.

    Draw the binary tree representation of the following arithmetic expression:
    “(((5 + 2) ∗ (2 − 1))/((2 + 9) + ((7 − 2) − 1)) ∗ 8)”.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------

                            '*'
                          /      \
                        '/'       8
                 /             \
                /               '+'
               /            /         \
             '*'          '+'         '-'
            /   \        /  \        /   \
          '+'    '-'    2    9     '-'     1
         /  \   /  \               /  \
        5    2 2    1             7    2
    """
    return True


class MutableLinkedBinaryTree(LinkedBinaryTree):
    """Solution to exercise R-8.15.

    The LinkedBinaryTree class provides only nonpublic versions of the up-
    date methods discussed on page 319. Implement a simple subclass named
    MutableLinkedBinaryTree that provides public wrapper functions for each
    of the inherited nonpublic update methods.
    """

    class _Node(LinkedBinaryTree._Node):
        def __hash__(self):
            """Ensure nodes are hashable for use in dictionaries."""
            return hash(id(self))

    def add_root(self, e):
        """Place element e at root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        return self._add_root(e)

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has left child.
        """
        return self._add_left(p, e)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has right child.
        """
        return self._add_right(p, e)

    def replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        return self._replace(p, e)

    def delete(self, p):
        """Delete node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        return self._delete(p)

    def attach(self, p, tree1, tree2):
        """Attach trees t1 and t2, respectively.

        Attach trees t1 and t2, respectively, as the left and right subtrees
        of the external Position p.
        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        self._attach(p, tree1, tree2)


class EulerTourLevelNumber(BinaryEulerTour):
    """Solution to exercise R-8.17.

    Show how to use the Euler tour traversal to compute the level number
    f(p), as defined in Section 8.3.2, of each position in a binary tree T.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I chose to use the previsit hook of the BinaryEulerTour class to implement
    my calculation of f(p).  My new class EulerTourLevelNumber inherits from
    BinaryEulerTour and overwrites its _hook_previsit() method to do so.  I
    also initialize the class with an empty dictionary fp_dict to keep track of
    the numbering of each node.  The dictionary stores the node (modified to be
    hashable) as a key, and the value is the node's corresponding f(p) value.

    I then unit test this solution by creating a binary tree with nodes
    containing a letter from the alphabet.  Each letter of the alphabet has an
    index in the alphabet that correspond's to the node's f(p) value.  I can
    then perform a Euler's tour of the binary tree and compare the resulting
    fp_dict f(p) values for the node with the expected f(p) value based on the
    node's label (letter from the alphabet).
    """

    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        super().__init__(tree)
        self.fp_dict = {}

    def _hook_previsit(self, p, d, path):
        """Visit Position p, before the tour of its children.

        p        Position of current position being visited
        d        depth of p in the tree
        path     list of indices of children on path from root to p
        """
        if d == 0:
            self.fp_dict[p._node] = d  # Root node
            return
        parent = p._node._parent
        if p._node == parent._left:
            self.fp_dict[p._node] = 2 * self.fp_dict[parent] + 1
        else:
            self.fp_dict[p._node] = 2 * self.fp_dict[parent] + 2


def preorder_postorder():
    r"""Solution to exercise R-8.20.

    Draw a binary tree T that simultaneously satisfies the following:
        • Each internal node of T stores a single character.
        • A preorder traversal of T yields EXAMFUN.
        • An inorder traversal of T yields MAFXUEN.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A binary tree is an ordered tree with the following properties:
        1. Every node has at most two children.
        2. Each child node is labeled as being either a left child or a right
           child.
        3. A left child precedes a right child in the order of children of a
           node.

    A preorder traversal starts at the root of the tree, and proceeds through
    the children in order which is left-to-right for a binary tree as defined
    in point (3) above.  The preorder traversal is recursively called on each
    child.  The following tree spells out EXAMFUN after a preorder
    traversal, but spells out AMXUNFE after a postorder traversal:

                            E
                         /     \
                        X       F
                       / \     / \
                      A   M   U   N

    A postorder traversal recursively traverses the subtrees rooted at the
    children of the root first, and then visits the root.  The following tree
    spells out MAFXUEN after a postorder traversal, but spells out NFMAEXU
    after a preorder traversal:

                            N
                         /     \
                        F       E
                       / \     / \
                      M   A   X   U

    Clearly, neither of these trees satisifes the conditions of the exercise.
    The trick is to pair letters together as siblings from right-to-left in
    the postorder string MAFXUEN, or pair letters together from the outside-in
    in the preorder string EXAMFUN.  The pairings are: EN, XU, AF, M in that
    order.

    However, the tree needs a root node, and a root can't have a sibling.  The
    requirements of the exercise state that internal nodes must have a single
    character, but no restrictions are placed on what characters can be used in
    the tree. To simultaneously satisfy the conditions of the exercise, I will
    use the empty string '' as the root node character:

                            ''
                         /     \
                        E       N
                       / \
                      X   U
                     /  \
                    A    F
                   /
                  M

    A preorder traversal of the above tree yields EXAMFUN, and a postorder
    traversal yields MAFXUEN.
    """
    return True


def preorder_fig8p8():
    """Solution to exercise R-8.21.

    In what order are positions visited during a preorder traversal of the tree
    of Figure 8.8?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A preorder traversal starts at the root of the tree, and proceeds through
    the children in order which is left-to-right for a binary tree.  The
    preorder traversal is recursively called on each child.  A preorder
    traversal of Figure 8.8 visits the nodes in the following order:

    - / x + 3 1 3 + - 9 5 2 + x 3 - 7 4 6

    Computing this expression using prefix notation:

    = (- (/ (x (+ 3 1) 3) (+ (- 9 5) 2)) (+ (x 3 (- 7 4)) 6))

    = (- (/ (x 4 3) (+ 4 2)) (+ (x 3 3) 6))

    = (- (/ 12 6) (+ 9 6))

    = (- 2 15)

    = -13

    """
    return -13


def postorder_fig8p8():
    """Solution to exercise R-8.22.

    In what order are positions visited during a postorder traversal of the
    tree of Figure 8.8?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A postorder traversal recursively traverses the subtrees rooted at the
    children of the root first, and then visits the root.  A postorder
    traversal of Figure 8.8 vists the nodes in the following order:

    3 1 + 3 x 9 5 - 2 + / 3 7 4 - x 6 + -

    Computing this expression using postfix notation:

    = ((((3 1 +) 3 x) ((9 5 -) 2 +) /) ((3 (7 4 -) x) 6 +) -)

    = (((4 3 x) (4 2 +) /) ((3 3 x) 6 +) -)

    = ((12 6 /) (9 6 +) -)

    = (2 15 -)

    = -13

    """
    return -13
