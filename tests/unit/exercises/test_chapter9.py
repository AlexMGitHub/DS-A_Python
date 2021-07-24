#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 9 exercises.

###############################################################################
# test_chapter9.py
#
# Revision:     1.00
# Date:         7/6/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 9 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
import dsa.chapter9_exercises as chap9
from dsa.chapter7_exercises import PositionalList


# %% Reinforcement Exercises
def test_remove_smallest_logn():
    """Solution to exercise R-9.1.

    How long would it take to remove the logn smallest elements from a
    heap that contains n entries, using the remove_min operation?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. remove_min is O(n) for an unsorted priority queue, and so it would
       require O(nlogn) time.

    2. remove_min is O(1) for a sorted priority queue, and so it would require
       O(logn) time.

    3. remove_min is O(logn) for a heap implementation of a priority queue, and
       so it would require O(logn * logn) time.
    """
    assert chap9.remove_smallest_logn()


def test_remove_min_calls():
    """Solution to exercise R-9.3.

    What does each remove min call return within the following sequence of
    priority queue ADT methods: add(5,A), add(4,B), add(7,F), add(1,D),
    remove min( ), add(3,J), add(6,L), remove min( ), remove min( ),
    add(8,G), remove min( ), add(2,H), remove min( ), remove min( )?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. Initial state                        {}
    2. add(5,A)                             {(5,A)}
    3. add(4,B)                             {(4,B), (5,A)}
    4. add(7,F)                             {(4,B), (5,A), (7,F)}
    5. add(1,D)                             {(1,D), (4,B), (5,A), (7,F)}
    6. remove_min()         (1,D)           {(4,B), (5,A), (7,F)}
    7. add(3,J)                             {(3,J), (4,B), (5,A), (7,F)}
    8. add(6,L)                             {(3,J), (4,B), (5,A), (6,L), (7,F)}
    9. remove_min()         (3,J)           {(4,B), (5,A), (6,L), (7,F)}
    10. remove_min()        (4,B)           {(5,A), (6,L), (7,F)}
    11. add(8,G)                            {(5,A), (6,L), (7,F), (8,G)}
    12. remove_min()        (5,A)           {(6,L), (7,F), (8,G)}
    13. add(2,H)                            {(2,H), (6,L) (7,F), (8,G)}
    14. remove_min()        (2,H)           {(6,L), (7,F), (8,G)}
    15. remove_min()        (6,L)           {(7,F), (8,G)}
    """
    expected_ans = ((1, 'D'), (3, 'J'), (4, 'B'), (5, 'A'), (2, 'H'), (6, 'L'))
    for answer, expected in zip(chap9.remove_min_calls(), expected_ans):
        assert answer == expected


def test_min_method_o1():
    """Solution to exercise R-9.5.

    The min method for the UnsortedPriorityQueue class executes in O(n)
    time, as analyzed in Table 9.2. Give a simple modification to the class so
    that min runs in O(1) time. Explain any necessary modifications to other
    methods of the class.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    I assume that the purpose of this question is to point out that a sorted
    priority queue's min() method runs in O(1) time.  The add() method could
    be modified to walk through the queue of values and add the new value to
    its appropriate place in the linked list - sorting the queue.

    Now the add() method will be O(n), but the min() method can run in O(1)
    time by simply returning the first item in the linked list.
    """
    assert chap9.min_method_o1()


def test_remove_min_method_o1():
    """Solution to exercise R-9.6.

    Can you adapt your solution to the previous problem to make remove min
    run in O(1) time for the UnsortedPriorityQueue class? Explain your an-
    swer.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    My solution to the previous problem was to have the add() method walk
    through the linked list representing the queue and add the new item at its
    appropriate (sorted) location.

    This solution allows us to simply remove the first item in the linked list,
    as it will be the minimum priority value in the queue.  This can be done in
    O(1) time.
    """
    assert chap9.remove_min_method_o1()


def test_selection_sort():
    """Solution to exercise R-9.7.

    Illustrate the execution of the selection-sort algorithm on the following
    input sequence: (22, 15, 36, 44, 10, 3, 9, 13, 29, 25).

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Selection-sort operates in two phases.  In phase 1, all of the elements
    in the input sequence S are removed and added to the priority queue PQ.
    In phase 2, the remove_min() method of the priority queue is called until
    PQ is empty, and each returned value is added back to the original sequence
    such that it is ordered.

    Assuming that phase 1 is complete, then S is now empty and PQ has all of
    S's elements inserted using the element as both the key and the value.
    Selection-sort implements PQ with an unsorted list, and so the elements
    are added in unsorted order to PQ in O(n) time:

    S = ()
    PQ = {22, 15, 36, 44, 10, 3, 9, 13, 29, 25}

    Phase 2 now calls remove_min() and places each of the elements back in S.
    Because PQ is implemented with an unsorted list, it must walk through
    each key in the queue looking for the minimum key which means phase 2 takes
    O(n^2) time:

    1.  S = (3)
        PQ = {22, 15, 36, 44, 10, 9, 13, 29, 25}

    2.  S = (3, 9)
        PQ = {22, 15, 36, 44, 10, 13, 29, 25}

    ...

    9.  S = (3, 9, 10, 13, 15, 22, 25, 29, 36)
        PQ = {44}

    10. S = (3, 9, 10, 13, 15, 22, 25, 29, 36, 44)
        PQ = {}


    And the selection-sort is complete in O(n^2) time.
    """
    sequence = (22, 15, 36, 44, 10, 3, 9, 13, 29, 25)
    sorted_sequence = sorted(list(sequence))
    collection = PositionalList()
    for x in sequence:
        collection.add_last(x)
    chap9.selection_sort(collection)
    for element, expected in zip(collection, sorted_sequence):
        assert element == expected


def test_insertion_sort():
    """Solution to exercise R-9.8.

    Illustrate the execution of the insertion-sort algorithm on the input se-
    quence of the previous problem.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Insertion-sort operates in two phases.  In phase 1, all of the elements
    in the input sequence S are removed and added to the priority queue PQ.
    In phase 2, the remove_min() method of the priority queue is called until
    PQ is empty, and each returned value is added back to the original sequence
    such that it is ordered.

    Assuming that phase 1 is complete, then S is now empty and PQ has all of
    S's elements inserted using the element as both the key and the value.
    Insertion-sort implements PQ with a sorted list, and so the elements
    are added in sorted order to PQ in O(n^2) worst-case time:

    S = ()
    PQ = {3, 9, 10, 13, 15, 22, 25, 29, 36, 44}

    Phase 2 now calls remove_min() and places each of the elements back in S.
    Because PQ is implemented with a sorted list, it can simply remove the
    first item in its linked list which means phase 2 takes O(n) time:

    1.  S = (3)
        PQ = {9, 10, 13, 15, 22, 25, 29, 36, 44}

    2.  S = (3, 9)
        PQ = {10, 13, 15, 22, 25, 29, 36, 44}

    ...

    9.  S = (3, 9, 10, 13, 15, 22, 25, 29, 36)
        PQ = {44}

    10. S = (3, 9, 10, 13, 15, 22, 25, 29, 36, 44)
        PQ = {}


    And the insertion-sort is complete in worst-case O(n^2) time, best-case
    O(n) time.
    """
    sequence = (22, 15, 36, 44, 10, 3, 9, 13, 29, 25)
    sorted_sequence = sorted(list(sequence))
    collection = PositionalList()
    for x in sequence:
        collection.add_last(x)
    chap9.insertion_sort(collection)
    for element, expected in zip(collection, sorted_sequence):
        assert element == expected


def test_worst_case_insertion_sort():
    """Solution to exercise R-9.9.

    Give an example of a worst-case sequence with n elements for insertion-
    sort, and show that insertion-sort runs in Ω(n^2) time on such a sequence.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The worst-case for insertion-sort occurs when the sequence S to be sorted
    is already sorted in reverse-order.  For example:

    S = (5, 4, 3, 2, 1)

    Insertion-sort implements the priority queue PQ with a sorted list, and so
    in phase 1 every time an element from S is added to PQ it will be sorted:

    0.  S = (5, 4, 3, 2, 1)
        PQ = {}

    1.  S = (5, 4, 3, 2)
        PQ = {1}

    2.  S = (5, 4, 3)
        PQ' = {2, 1}
        PQ  = {1, 2}

    3.  S = (5, 4)
        PQ' = {3, 1, 2}
        PQ  = {1, 2, 3}

    4.  S = (5)
        PQ' = {4, 1, 2, 3}
        PQ  = {1, 2, 3, 4}

    5.  S = ()
        PQ' = {5, 1, 2, 3, 4}
        PQ  = {1, 2, 3, 4, 5}


    I am assuming that elements are removed from the right of S and added to
    the left of PQ.  Every time an element is added to PQ, it must be shifted
    all the way to the end of the linked list to be sorted in its proper place.
    Every item added to the linked list grows its length by one, and so each
    successive call to add() requires one more operation than the last call.

    This results in operations proportional to the sum of the first n integers,
    and so phase 1 must be Ω(n^2).  Phase 2 simply removes the items from PQ
    and adds them back into S, which can be performed in O(n) time as PQ is
    already sorted.  Because of this, phase 1 dominates the performance of
    insertion-sort, and in the case where the sequence S is sorted in reverse-
    order the running-time of insertion-sort is Ω(n^2).
    """
    assert chap9.worst_case_insertion_sort()


def test_heap_third_smallest():
    """Solution to exercise R-9.10.

    At which positions of a heap might the third smallest key be stored?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A heap has the following properties:
    1. Complete binary tree property: all levels of the tree from 0 to h-1 must
       have the maximum number of nodes possible; remaining nodes at h must be
       the left-most possible nodes.
    2. Heap-order property: For every position p other than the root, the key
       stored at p is greater than or equal to the key stored at p's parent.

    Based on these two properties, we know the following:
    1. The smallest key must be at the root (level 0), and both children of the
       root must be filled if there are three or more items.
    2. The third smallest key may be either the left or right child of the root
       (level 1) as that would satisfy the heap-order property.
    3. The third smallest key can only be on level 2 if it is the child of the
       second smallest key, otherwise it would violate the heap-order property.

    So the third smallest key could be:
    1. The left or right child of the root
    2. The left or right child of the second smallest key, which in turn must
       be the left or right child of the root.
    """
    assert chap9.heap_third_smallest()


def test_heap_largest():
    """Solution to exercise R-9.11.

    At which positions of a heap might the largest key be stored?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The largest key must be a leaf node, because if it were a parent it would
    violate the heap-order property.
    """
    assert chap9.heap_largest()


def test_max_oriented():
    """Solution to exercise R-9.12.

    Consider a situation in which a user has numeric keys and wishes to have
    a priority queue that is maximum-oriented. How could a standard (min-
    oriented) priority queue be used for such a purpose?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. If the priority queue is unsorted, the keys of the items could be
       stored as -1 * key.   This ensures that the largest magnitude key is
       stored at the beginning of the queue, because it will evaluate as the
       smallest negative number.

    2. If the priority queue is sorted, the max() function could simply return
       the item contained in the last node of the underlying linked list.

    3. If the priority queue is implemented as a heap, option (1) would work.
    """
    assert chap9.max_oriented()


def test_in_place_heap_sort():
    r"""Solution to exercise R-9.13.

    Illustrate the execution of the in-place heap-sort algorithm on the
    following input sequence: (2, 5, 16, 4, 10, 23, 39, 18, 26, 15).

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    Phase 1 of the in-place heap-sort moves left-to-right through the sequence,
    adding each element to a maximum-oriented heap.  Each new item is inserted
    into the heap at either the left-most position of a new level, or the
    right-most position of an existing level.  Each new item is up-heap bubbled
    by swapping positions with its parent node until its key is less than its
    parent's key (for a maximum-oriented heap).

    At the end of phase 1 we will have the sequence S and heap shown below:

    (2, 5, 16, 4, 10, 23, 39, 18, 26, 15)
                                       ^
                        39
                     /      \
                   26        23
                 /    \    /    \
                18    15  5     16
               / \    /
              2  10  4

    The caret under the value 15 indicates that the current index position
    corresponds to 15, i.e. the index is n-1 = 9.  We now begin phase 2, where
    we remove the maximum key from the heap and place it at the index n-i for
    steps i = 1, 2, ..., n.  Each time the root is removed from the heap, it is
    replaced by the last node in the heap - that is the bottom-most and right-
    most node in the heap.  The new root is then down-heap bubbled until
    its children have keys smaller than its key (for a maximum oriented heap).
    We always choose to swap nodes with the child with the larger key.

    1.  Step i = 1:
        39 goes to index n-1 = 9
        39 swaps with 15, now index 9 from index 6
        4 moved to root
        4 swaps with 26, now index 8 from index 3
        4 swaps with 18, now index 7 from index 8
        4 swaps with 10, now index 4 from index 7

    (2, 5, 16, 26, 4, 23, 15, 10, 18, 39)
                                   ^
                        26
                     /      \
                   18        23
                 /    \    /    \
                10    15  5     16
               / \
              2  4

    2.  Step i = 2:
        26 goes to index n-2 = 8
        26 swaps with 18, now index 8 from index 3
        4 moved to root
        4 swaps with 23, now index 5 from index 4
        4 swaps with 16, now index 2 from index 5

    (2, 5, 4, 18, 23, 16, 15, 10, 26, 39)
                               ^
                        23
                     /      \
                   18        16
                 /    \    /    \
                10    15  5     4
               /
              2

    3.  Step i = 3:
        23 goes to index n-3 = 7
        23 swaps with 10, now index 7 from index 4
        2 moved to root
        2 swaps with 18, now index 3 from index 0
        2 swaps with 15, now index 6 from index 3

    (18, 5, 4, 15, 10, 16, 2, 23, 26, 39)
                           ^
                        18
                     /      \
                   15        16
                 /    \    /    \
                10    2   5     4

    4.  Step i = 4:
        18 goes to index n-4 = 6
        18 swaps with 2, now index 6 from index 0
        4 moved to root
        4 swaps with 16, now index 5 from index 2
        4 swaps with 5, now index 1 from index 5

    (2, 4, 16, 15, 10, 5, 18, 23, 26, 39)
                       ^
                        16
                     /      \
                   15        5
                 /    \    /    \
                10    2   4

    5.  Step i = 5:
        16 goes to index n-5 = 5
        16 swaps with 5, now index 5 from index 2
        4 moved to root
        4 swaps with 15, now index 3 from index 1
        4 swaps with 10, now index 4 from index 3

    (2, 15, 5, 10, 4, 16, 18, 23, 26, 39)
                   ^
                        15
                     /      \
                   10        5
                 /    \    /    \
                4      2

    6.  Step i = 6:
        15 goes to index n-6 = 4
        15 swaps with 4, now index 4 from index 1
        2 moved to root
        2 swaps with 10, now index 3 from index 0
        2 swaps with 4, now index 1 from index 3

    (10, 2, 5, 4, 15, 16, 18, 23, 26, 39)
               ^
                        10
                     /      \
                   4         5
                 /    \    /    \
                2

    7.  Step i = 7:
        10 goes to index n-7 = 3
        10 swaps with 4, now index 3 from index 0
        2 moved to root
        2 swaps with 5, now index 2 from index 1

    (4, 5, 2, 10, 15, 16, 18, 23, 26, 39)
           ^
                        5
                     /      \
                   4         2

    8.  Step i = 8:
        5 goes to index n-8 = 2
        5 swaps with 2, now index 2 from index 1
        2 moved to root
        2 swaps with 4, now index 0 from index 1

    (2, 4, 5, 10, 15, 16, 18, 23, 26, 39)
        ^
                        4
                     /      \
                   2

    9.  Step i = 9:
        4 goes to index n-9 = 1
        No swap needed
        2 moved to root
        No swap needed

    (2, 4, 5, 10, 15, 16, 18, 23, 26, 39)
     ^
                        2
    10. Step i = 10:
        2 goes to index n-10 = 0
        No swap needed
        Heap empty

    (2, 4, 5, 10, 15, 16, 18, 23, 26, 39)


    And the sequence has been sorted in-place.
    """
    assert chap9.in_place_heap_sort()


def test_is_tree_heap():
    r"""Solution to exercise R-9.14.

    Let T be a complete binary tree such that position p stores an element
    with key f(p), where f(p) is the level number of p (see Section 8.3.2).
    Is tree T a heap? Why or why not?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A complete binary tree has all levels 0 through h-1 filled with the maximum
    number nodes possible, and the remaining nodes on level h reside at the
    left-most possible positions.

    The level numbering function f(p) is calculated according to three rules:
    1. If p is root of T, f(p) = 0
    2. If p is left child of q, then f(p) = 2*f(q) + 1
    3. If p is right child of q, then f(p) = 2*f(q) + 2

    A complete binary tree storing f(p) for the keys of each node would look
    like the tree below for n = 5:

                          0
                       /    \
                      1      2
                     / \    / \
                    3   4

    A heap must satisfy two properties:
    1. The heap-order property: For every position p except for the root, the
       key stored at p is greater than or equal to the key stored at p's parent

    2. Complete binary tree property: Explained above.

    Property (2) was specified in the formulation of the question and so is
    satisfied, and property (1) is also satisfied because f(p) is calculated
    such that the child nodes will always have keys greater than their parent
    node.  Therefore tree T is a heap.
    """
    assert chap9.is_tree_heap()


def test_no_right_child():
    """Solution to exercise R-9.15.

    Explain why the description of down-heap bubbling does not consider the
    case in which position p has a right child but not a left child.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A heap that has a right child - but not a left child - violates the
    Complete Binary Tree Property which requires that the left-most possible
    nodes be filled first.
    """
    assert chap9.no_right_child()
