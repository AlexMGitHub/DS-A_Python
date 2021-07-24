#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 15 exercises.

###############################################################################
# test_chapter15.py
#
# Revision:     1.00
# Date:         7/20/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 15 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
import dsa.chapter15_exercises as chap15


# %% Reinforcement Exercises
def test_upgrade_main_memory():
    """Solution to exercise R-15.1.

    Julia just bought a new computer that uses 64-bit integers to address mem-
    ory cells. Argue why Julia will never in her life be able to upgrade the
    main memory of her computer so that it is the maximum-size possible,
    assuming that you have to have distinct atoms to represent different bits.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A 64-bit integer can address 2^64 = 18,446,744,073,709,551,616 memory
    cells.  If we assume each memory cell stores a 64-bit word, then the
    maximum size of the main memory of Julia's computer is a total of 2^128
    bits of data

    The average diameter of an atom is on the order of 0.1 nanometers.
    If we assume that each bit of the memory can be represented by a single
    atom, then the physical volume that the maximized memory would occupy is:

    = (2^128 bits) * (1 atom per bit) * (volume of atom)

    = (2^128 atoms) * (volume of atom)

    = (2^128 atoms) * ((4/3)*pi*r^3 meters cubed per atom)

    = (2^128 atoms) * ((4/3)*pi*(0.5*10^-10)^3 m^3 per atom)

    = 1.78 * 10^8 meters cubed

    Julia's goal of uprading the main memory of her computer to its
    maximum-size possible is not feasible.
    """
    assert chap15.upgrade_main_memory()


def test_ab_values():
    """Solution to exercise R-15.3.

    Suppose T is a multiway tree in which each internal node has at least five
    and at most eight children. For what values of a and b is T a valid (a, b)
    tree?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Per the Size Property of (a,b) trees, an internal node has at least 'a'
    children, unless it is the root, and has at most 'b' children.
    However, a valid (a, b) tree constrains 'a' as follows:

        2 <= a <= (b+1)/2

    If 'a' is set to 5 and 'b' is set to 8, this inequality is violated as an
    'a' of 5 exceeds the upper bound of (8+1)/2 = 4.5.  This means 'b' has to
    be at least 9 if 'a' is 5.  However, the value of 'a' can also be less than
    5 so long as it is at least 2.  In this case 'b' could be 8 as it would
    satisfy both the Size Property and the inequality above.

    The values of 'a' and 'b' can thus be:

    (a, b) can be any of (2, 8+), (3, 8+), (4, 8+), or (5, 9+).

    Where the 'b' values shown are the minimum 'b' values, i.e. 'b' must be
    greater than or equal to the values given.
    """
    assert chap15.ab_values()


def test_order_d_btree():
    """Solution to exercise R-15.4.

    For what values of d is the tree T of the previous exercise an order-d
    B-tree?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A B-tree of order d is an (a, b) tree with a = ceil(d/2) and b = d.
    This sets an upper limit on the value of 'b', because as 'b' increases 'a'
    increases, too.  Whereas for an (a, b) tree 'a' simply need to be less
    than or equal to 'b' and greater than or equal to 2.

    The value of 'a' represents the minimum number of children that internal
    nodes must have, and so we know that 'd' cannot be larger than 10 so that
    'a' is not larger than 5 and thus violate the Size Property.  'd' cannot be
    smaller than 8, because that would also violate the Size Property with
    respect to 'b'.

    The resulting valid values of 'd' are: 8, 9, 10

    This results in (a, b) values of (4, 8), (5, 9), (5, 10)

    The tree T from the previous exercise had between 5 and 8 nodes, and is
    still a valid (a, b) tree for the above values of 'd'.
    """
    assert chap15.order_d_btree()


def test_number_page_misses_lru():
    """Solution to exercise R-15.5.

    Consider an initially empty memory cache consisting of four pages. How
    many page misses does the LRU algorithm incur on the following page
    request sequence: (2, 3, 4, 1, 2, 5, 1, 3, 5, 4, 1, 2, 3)?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The LRU algorithm uses an adaptable priority queue to evict the page that
    is least-recently used when a new page request is received and the cache is
    full.

    I assume from the context that a page miss occurs whenever the page
    request results in an access to external (slower) memory rather than
    responding with a page from the cache.

    The first four requests will result in page misses because the memory cache
    m is initially empty.  After the first four requests m is as below:

    Next pages      = (2, 3, 4, 1)
    Page misses     = 4
    m               = { 2,  3,  4,  1}
    Priority        = {-4, -3, -2, -1}

    I have written the priority below the values in the queue to avoid
    confusion between the values themselves and their respective priority.  The
    most recently accessed page (1) has a priority of -1 as it was the last
    accessed page in the cache.  It thus has the highest priority and will not
    be evicted until its priority drops to the lowest value.  The lowest
    priority -4 is assigned to page (2) as it was the least-recently accessed
    page in the cache.  It will be the next page to be evicted unless it is
    accessed again before a new page is requested.

    Next page       = 2
    Page misses     = 4
    m               = { 2,  3,  4,  1}
    Priority        = {-1, -4, -3, -2}

    (2) was already in the cache, and so there was no page miss and (2)'s
    priority increased to -1, while the priorities of all other values
    decreased by one.

    Next page       = 5
    Page misses     = 5
    m               = { 2,  5,  4,  1}
    Priority        = {-2, -1, -4, -3}

    (5) was not in the cache, and so there was a page miss.  (3) had the lowest
    priority and was evicted and replaced by (5), which has the highest
    priority as it was most recently accessed.  All other values had their
    priorities decreased by one.

    Next page       = 1
    Page misses     = 5
    m               = { 2,  5,  4,  1}
    Priority        = {-3, -2, -4, -1}

    Next page       = 3
    Page misses     = 6
    m               = { 2,  5,  3,  1}
    Priority        = {-4, -3, -1, -2}

    Next page       = 5
    Page misses     = 6
    m               = { 2,  5,  3,  1}
    Priority        = {-4, -1, -2, -3}

    Next page       = 4
    Page misses     = 7
    m               = { 4,  5,  3,  1}
    Priority        = {-1, -2, -3, -4}

    Next page       = 1
    Page misses     = 7
    m               = { 4,  5,  3,  1}
    Priority        = {-2, -3, -4, -1}

    Next page       = 2
    Page misses     = 8
    m               = { 4,  5,  2,  1}
    Priority        = {-3, -4, -1, -2}

    Next page       = 3
    Page misses     = 9
    m               = { 4,  3,  2,  1}
    Priority        = {-4, -1, -2, -3}


    I count 9 page misses using the LRU algorithm.
    """
    assert chap15.number_page_misses_lru()


def test_number_page_misses_fifo():
    """Solution to exercise R-15.6.

    Consider an initially empty memory cache consisting of four pages. How
    many page misses does the FIFO algorithm incur on the following page
    request sequence: (2, 3, 4, 1, 2, 5, 1, 3, 5, 4, 1, 2, 3)?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The FIFO algorithm uses a queue to evict the page that was transferred to
    the cache furthest in the past when a new page request is received and the
    cache is full.

    I assume from the context that a page miss occurs whenever the page
    request results in an access to external (slower) memory rather than
    responding with a page from the cache.

    The first four requests will result in page misses because the memory cache
    m is initially empty.  After the first four requests m is as below:

    Next pages      = (2, 3, 4, 1)
    Page misses     = 4
    m               = {2, 3, 4, 1}

    The queue proceeds right to left; that is pages exit the queue from its
    front on the left, and pages enter the queue from its back on the right.
    The left-most item in the queue is the first page in and will be the
    page evicted on a page miss.

    Next page       = 2
    Page misses     = 4
    m               = {2, 3, 4, 1}

    Next page       = 5
    Page misses     = 5
    m               = {3, 4, 1, 5}

    The queue didn't change when page (2) was requested, because it existed in
    cache and so there was no page miss.  When (5) was requested, page (2)
    was evicted as it was at the front of the queue.  (5) was then added at the
    back of the queue.

    Next page       = 1
    Page misses     = 5
    m               = {3, 4, 1, 5}

    Next page       = 3
    Page misses     = 5
    m               = {3, 4, 1, 5}

    Next page       = 5
    Page misses     = 5
    m               = {3, 4, 1, 5}

    Next page       = 4
    Page misses     = 5
    m               = {3, 4, 1, 5}

    Next page       = 1
    Page misses     = 5
    m               = {3, 4, 1, 5}

    Next page       = 2
    Page misses     = 6
    m               = {4, 1, 5, 2}

    Next page       = 3
    Page misses     = 7
    m               = {1, 5, 2, 3}


    I count 7 page misses using the FIFO algorithm.
    """
    assert chap15.number_page_misses_fifo()


def test_number_page_misses_random():
    """Solution to exercise R-15.7.

    Consider an initially empty memory cache consisting of four pages. What
    is the maximum number of page misses that the random algorithm incurs
    on the following page request sequence: (2, 3, 4, 1, 2, 5, 1, 3, 5, 4, 1,
    2, 3)?
    Show all of the random choices the algorithm made in this case.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The random algorithm uses a pseudo-random number generator to choose which
    page to evict when a new page request is received and the cache is full.

    I assume from the context that a page miss occurs whenever the page
    request results in an access to external (slower) memory rather than
    responding with a page from the cache.

    I randomly generated a sequence of 9 random integers with values between
    1 and 4 to represent the 4 indices of m.  I will not need 13 indices as the
    first four page requests will be stored in the empty cache.  I may not need
    all of the remaining 9 indices, and so will use them in order from left to
    right as needed.  The randomly selected indices are below:

        [1, 4, 3, 2, 3, 4, 1, 1, 4]

    The cache m begins as an empty list, and new pages are appended to the
    end of m until len(m) == 4, at which point new pages will cause a
    randomly selected page to be evicted.

    The first four requests will result in page misses because the memory cache
    m is initially empty.  After the first four requests m is as below:

    Next pages      = (2, 3, 4, 1)
    Page misses     = 4
    m               = [2, 3, 4, 1]

    The indices for m proceed left to right, starting with index 1 at value (2)
    and ending at index 4 with value (1).

    Next page       = 2
    Page misses     = 4
    Random index    =
    m               = [2, 3, 4, 1]

    Next page       = 5
    Page misses     = 5
    Random index    = 1
    m               = [5, 3, 4, 1]

    The first random index is 1, which means that page (2) is replaced by the
    new page (5).

    Next page       = 1
    Page misses     = 5
    Random index    =
    m               = [5, 3, 4, 1]

    Next page       = 3
    Page misses     = 5
    Random index    =
    m               = [5, 3, 4, 1]

    Next page       = 5
    Page misses     = 5
    Random index    =
    m               = [5, 3, 4, 1]

    Next page       = 4
    Page misses     = 5
    Random index    =
    m               = [5, 3, 4, 1]

    Next page       = 1
    Page misses     = 5
    Random index    =
    m               = [5, 3, 4, 1]

    Next page       = 2
    Page misses     = 6
    Random index    = 4
    m               = [5, 3, 4, 2]

    Next page       = 3
    Page misses     = 6
    Random index    =
    m               = [5, 3, 4, 2]


    I count 6 page misses using the random algorithm.
    """
    assert chap15.number_page_misses_random()


def test_insert_keys_btree():
    r"""Solution to exercise R-15.8.

    Draw the result of inserting, into an initially empty order-7 B-tree,
    entries with keys (4, 40, 23, 50, 11, 34, 62, 78, 66, 22, 90, 59, 25, 72,
    64, 77, 39, 12), in this order.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A B-tree of order d is an (a, b) tree with a = ceil(d/2) and b = d.
    An order-7 B-tree has b = d = 7 and a = ceil(b/2) = ceil(7/2) = 4.

    Per the Size Property of (a,b) trees, an internal node has at least 'a'
    children, unless it is the root, and has at most 'b' children.
    Per the depth property, all external nodes must have the same depth.

    This means each node must have at least 4 children and no more than 7
    children.  The node itself can store between a-1 = 3 entries and b-1 = 6
    entries.

    We will insert the first 3 keys to ensure the root has the minimum required
    number of entries:

                            (4, 23, 40)
                           /   /   \   \

    The root node has 3 entries in sorted order and 4 children.  We will
    continue adding keys until the root node becomes an illegal (d+1)-node,
    meaning it has 7+1=8 children:

                            (4, 11, 23, 34, 40, 50, 62)
                           /   |   |   |   |   |   |   \

    The root node now has 8 children.  The median value of the node will become
    the new root node, and the remaining values will be split into two nodes,
    one containing floor((d+1)/2) children an the other node containing
    ceil((d+1)/2) children:

                                       34
                                     /    \
                          (4, 11, 23)      (40, 50, 62)
                          /  |   |  \      /   |   |   \


    Next we insert keys 78, 66, 22, 90, and 59 until we again have an illegal
    node:

                                       34
                                     /    \
                     (4, 11, 22, 23)      (40, 50, 59, 62, 66, 78, 90)
                     /  |   |   |   \     /   |   |   |   |   |   |   \


    The median value of the node goes to the root node, and it splits:

                                    (34, 62)
                            /           |          \
            (4, 11, 22, 23)       (40, 50, 59)     (66, 78, 90)
            /  |   |   |   \      /   |   |   \    /   |   |   \


    Adding keys 25, 72, 64, 77, 39, and 12:

                                      (34, 62)
                            /             |           \
    (4, 11, 12, 22, 23, 25)       (39, 40, 50, 59)     (64, 66, 72, 77, 78, 90)
    /  |   |   |   |   |  \       /   |   |   |   \    /   |   |   |   |   |  \


    This is the final result of the order-7 B-tree after inserting the
    sequence of keys.  There are 4 internal nodes, all external nodes are on
    the same level, no node has more than d = 7 children, no node has fewer
    than a=4 children except for the root node, and no node has more
    than d-1=6 keys or fewer than a-1=3 keys, except for the root node.

    This satisfies all of the requirements of a B-tree.
    """
    assert chap15.insert_keys_btree()
