#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 12 exercises.

###############################################################################
# chapter12_exercises.py
#
# Revision:     1.00
# Date:         7/12/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 12 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports


# %% Reinforcement Exercises
def prop_12p1():
    """Solution to exercise R-12.1.

    Give a complete justification of Proposition 12.1.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Proposition 12.1 asserts the following:

    The merge-sort tree associated with an execution of merge-sort on a
    sequence of size n has height ceil(logn).

    The merge-sort tree is a binary tree where each node represents a recursive
    call of the merge-sort algorithm.  Each time merge-sort is called, it
    splits the input sequence into two (roughly) equal halves until the input
    sequence is of length 1.  The original sequence S is the root node of the
    binary tree, while the individual elements of S form the leaves of the
    binary tree.

    If the length of the sequence is not a power of 2, then there will be
    splits where one half will equal n//2, and the other half n//2 + 1.
    The length of the sequence at each node is thus either 2^h or 2^h + 1,
    where h is the height of the node.  This means that not all of the leaf
    nodes will be at the same depth, as an extra split operation is necessary
    for nodes containing n//2 + 1 elements.

    Leaf nodes have height 0, and 2^0 = 1 so the sequence will be length of 1.
    This matches our expectation that leaves contain a single element.
    The root node containing the original sequence must be length n, and the
    height of the root node (h_root) is the same as the height of the tree.

    Because n may not be a power of 2, 2^h_root may be greater than or equal to
    the number of elements in sequence S.  However, height must be an integer
    and so any decimal result for h_root should thus take the ceiling of the
    value.

    Therefore:

    2^(h_root) >= n
    h_root >= log(n)
    h_root = ceil(log(n))
    """
    return True


def merge_sort_arrows():
    """Solution to exercise R-12.2.

    In the merge-sort tree shown in Figures 12.2 through 12.4, some edges are
    drawn as arrows. What is the meaning of a downward arrow? How about
    an upward arrow?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    A downward arrow represents a recursive call to merge_sort(), splitting the
    sequence into two halves.  An upward arrow represents a call to merge(),
    which merges two sorted sequences back into the parent node that represents
    the original sequence they were split from.
    """
    return True


def merge_sort_stable():
    """Solution to exercise R-12.4.

    Is our array-based implementation of merge-sort given in Section 12.2.2
    stable? Explain why or why not.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Let S1 = [2, 3, 5] and S2 = [2, 4, 6].  Both are sorted sequences that
    contain the duplicate key 2.  Recall that S1 is composed of keys from the
    left half of S, and S2 of keys from the right half of S.  If a duplicate
    key exists in both S1 and S2, the duplicate key in S1 must have preceded
    the key in S2.  In order for a sort to be stable, this order must be
    maintained in the sorted list.

    When viewing the source code of merge() on page 543 of the text, the
    comparison between S1 and S2 is written using the < operator:

    S1[i] < S2[j]

    If True, element i from S1 is copied to S.  If False, element j from S2 is
    copied to S instead.  If i = j = 0 then:

    S1[0] < S2[0]
    2 < 2

    This statement is False, 2 is not less than itself.  Therefore S2[0] will
    be copied to S before S1[0].  As mentioned above, duplicates from S1 should
    be copied to S first because they preceded the duplicates in S2 in the
    original sequence.  Therefore this implementation of merge-sort is NOT
    stable.  However, if the comparison operator were changed to <= the merge-
    sort algorithm would be stable.
    """
    return True


def linked_list_stable():
    """Solution to exercise R-12.5.

    Is our linked-list-based implementation of merge-sort given in Code
    Fragment 12.3 stable? Explain why or why not.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    No, it is NOT stable for the same reason as exercise R-12.4.  The merge()
    function again compares S1 to S2 using the < operator:

    S1.first() < S2.first()

    If True, S1's element is copied to S, and if False S2's element is copied
    to S.  Again, in the case that S1.first() == S2.first() then S2's element
    will be copied to S before S1's element.  This will not maintain the
    original order of the duplicate keys in the sorted sequence.
    """
    return True


def sequence_union(A, B):
    """Solution to exercise R-12.7.

    Suppose we are given two n-element sorted sequences A and B each with
    distinct elements, but potentially some elements that are in both
    sequences.  Describe an O(n)-time method for computing a sequence
    representing the union A ∪ B (with no duplicates) as a sorted sequence.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Important information:
    1. A and B are both length n
    2. A and B are both sorted
    3. The elements of A and B are distinct, meaning no repeats within A or B

    Because the lists are sorted, we don't need to compare every element in
    A to every element in B.  We know that if A[i] < B[j] that we can increment
    i until A[i] >= B[j].  Conversely, if A[i] > B[j] we should increment j
    until A[i] <= B[j].  If a match is found, we append it to the union list
    and increment both i and j.  Because both A and B are distinct there is
    no possibility of getting multiple matches of the same value.

    The while loop will continue so long as both i and j are < n.  This means
    that the maximum number of loops is 2n.  Each loop performs an O(1)
    operation (append is O(1)* amortized), and so the algorithim's run-time
    efficiency is proportional to the number of loops, which is O(n).
    """
    union = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1                  # A values too low, skip ahead through A
        elif A[i] == B[j]:
            union.append(A[i])      # Values match, add to union list
            i += 1
            j += 1
        else:
            j += 1                  # B values too low, skip ahead through B
    return union


def quick_sort_pivot1():
    """Solution to exercise R-12.8.

    Suppose we modify the deterministic version of the quick-sort algorithm
    so that, instead of selecting the last element in an n-element sequence as
    the pivot, we choose the element at index n//2. What is the running time
    of this version of quick-sort on a sequence that is already sorted?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    If the pivot is always selected at n // 2, and the sequence is already
    sorted, then the pivot will be the median value of the sequence and split
    it evenly into two halves at every recursive call of quick_sort().
    This is the ideal scenario as the resulting quick-sort binary tree will
    have a height of log(n), and so the quick-sort algorithm's run-time will be
    O(nlogn).
    """
    return True


def quick_sort_pivot2():
    """Solution to exercise R-12.9.

    Consider a modification of the deterministic version of the quick-sort
    algorithm where we choose the element at index n//2 as our pivot.
    Describe the kind of sequence that would cause this version of quick-sort
    to run in Ω(n^2) time.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The sequence would need to ensure that the pivot value selected at index
    n // 2 was always either the smallest or the largest value in the sequence.
    This ensures that all values are moved to either L or G for every split,
    and so the sequence is only decreasing in length by 1 (the pivot value).
    This would cause the height of the tree to be n, and so the quick-sort
    algorithm's run-time would be Ω(n^2).

    To create this sequence, simply sort the values in reverse order, split
    the sequence in two, and then swap the two halves.  An example is shown
    below:

    [0 1 2 3 4 5 6 7 8 9]       # Example sequence
    [9 8 7 6 5 4 3 2 1 0]       # Reverse sort
    [4 3 2 1 0 9 8 7 6 5]       # Swap halves

    Now to demonstrate that the length of the sequence will only decrease by 1
    for each quick-sort call.  Remember, if the pivot value is the smallest or
    greatest value, all of the other values are placed into either L or G:

    [4 3 2 1 0 9 8 7 6 5]       # n = 10, n//2 = 5, pivot = 9, all values in L
    [4 3 2 1 0 8 7 6 5]         # n =  9, n//2 = 4, pivot = 0, all values in G
    [4 3 2 1 8 7 6 5]           # n =  8, n//2 = 4, pivot = 8, all values in L
    [4 3 2 1 7 6 5]             # n =  7, n//2 = 3, pivot = 1, all values in G
    [4 3 2 7 6 5]               # n =  6, n//2 = 3, pivot = 7, all values in L
    [4 3 2 6 5]                 # n =  5, n//2 = 2, pivot = 2, all values in G
    [4 3 6 5]                   # n =  4, n//2 = 2, pivot = 6, all values in L
    [4 3 5]                     # n =  3, n//2 = 1, pivot = 3, all values in G
    [4 5]                       # n =  2, n//2 = 1, pivot = 5, all values in L
    [4]                         # n <  2, Return
    """
    return True


def inplace_flaw():
    """Solution to exercise R-12.12.

    If the outermost while loop of our implementation of inplace quick sort
    (line 7 of Code Fragment 12.6) were changed to use condition left < right
    (rather than left <= right), there would be a flaw. Explain the flaw and
    give a specific input sequence on which such an implementation fails.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    This change would prevent the left index from exceeding the right index.
    The value at the left index and the pivot are swapped at the end of the
    quick-sort call.  This means that the wrong value will be swapped with the
    pivot.

    This is an issue whenever the value that the left and right indices meet at
    is less than the pivot value.  This value will end up on the right side of
    the sequence when it is swapped with the pivot (assuming we use the last
    element of the sequence as the pivot), when it should be on the left side
    of the sequence.

    The sequence used in Figure 12.14 works as an example.  The beginning
    sequence is [85, 24, 63, 45, 17, 31, 96, 50].  After the inplace quick-sort
    with the < operator, the result is [17, 31, 24, 50, 45, 63, 85, 96].

    [85, 24, 63, 45, 17, 31, 96, 50]  # Original sequence
                 l,r              p

    [31, 24, 17, 50, 63, 85, 96, 45]  # 50 at index 3
                  p

    [31, 24, 17]    [63, 85, 96, 45]
     l,r      p      l,r          p

    [17, 24, 31]    [45, 85, 96, 63]  # 17 at index 0, 45 at index 4
      p               p

        [24, 31]        [85, 96, 63]
         l,r  p          l,r      p

        [31, 24]        [63, 96, 85]  # 31 at index 1, 63 at index 5
          p               p

            [24]            [96, 85]  # 24 at index 2
              p              l,r  p

                            [85, 96]  # 85 at index 6
                              p

                                [96]  # 96 at index 7
                                  p

    [17, 31, 24, 50, 45, 63, 85, 96]

    The final sorted sequence is clearly incorrect.
    """
    return True


def bucket_sort_inplace():
    """Solution to exercise R-12.17.

    Is the bucket-sort algorithm in-place? Why or why not?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    An algorithm is in-place if uses only a small amount of memory in addition
    to that needed for the original input.  Bucket-sort uses a separate bucket
    array to store entries from the original sequence S.  The bucket array's
    memory usage must be at least as large as S in order to store all of S's
    entries.  The entries are then placed back into S in sorted order.

    Therefore bucket-sort requires O(n) additional memory usage and is *not*
    in-place.
    """
    return True


def radix_sort_triplets(sequence, N):
    """Solution to exercise R-12.18.

    Describe a radix-sort method for lexicographically sorting a sequence S of
    triplets (k, l, m), where k, l, and m are integers in the range [0, N − 1],
    for some N ≥ 2. How could this scheme be extended to sequences of d-tuples
    (k1, k2 , ..., kd), where each ki is an integer in the range [0, N − 1]?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The radix-sort of a sequence of d-tuples is simply the application of d
    bucket-sorts of the sequence in reverse order of keys.  In a lexicographic
    sort the dth key is the least important, and the first key the most
    important.  By stably sorting by the dth key first, then the d-1 key, d-2
    key, etc. we ensure a lexicographic ordering of the d-tuples.

    The solution below lexicographically sorts a sequence of d-tuples for any
    value of d > 0.  Note that I used a list of lists to represent the bucket
    array.  Popping and appending at the end of a list are O(1) operations,
    while popping and inserting at the beginning of a list are O(n) operations.

    Because of this, I iterate through the sequence of d-tuples in reverse
    order so that I can pop the last d-tuple from the sequence and append it to
    the end of the bucket at the appropriate index.  This inserts the d-tuples
    in the bucket in reverse order, such that d-tuples that appeared later in
    the sequence are stored in the beginning of the bucket.

    Once the sequence is empty, I iterate through the bucket array in order
    from index 0 to N-1.  I again pop d-tuples from the end of each bucket and
    append them to the end of the sequence.  The d-tuples at the end of the
    bucket are the d-tuples that appeared earliest in the sequence, and so
    this preserves the order of the entries in the sequence (stable) while
    allowing for O(1) array operations.

    This is the reverse of the front-to-back method discussed in the text,
    where the sequence is accessed front-to-back and elements are removed from
    the buckets front-to-back.  Because I operate back-to-front on both the
    sequence and the buckets the reversal cancels out, and the result is a
    stable sort.

    This series of operations repeats for all d keys in the tuple.
    """
    bucket_array = [[] for _ in range(N)]
    d = len(sequence[0])
    n = len(sequence)
    for key_idx in range(d-1, -1, -1):      # Start with last key in d-tuple
        for tup_idx in range(n-1, -1, -1):  # Reverse order so we can pop()
            key = sequence[tup_idx][key_idx]
            bucket_array[key].append(sequence.pop(tup_idx))
        for bkt_idx in range(N):
            for _ in range(len(bucket_array[bkt_idx])):
                sequence.append(bucket_array[bkt_idx].pop())  # Pop again


def how_long_quick_merge_sorts():
    """Solution to exercise R-12.19.

    Suppose S is a sequence of n values, each equal to 0 or 1. How long will
    it take to sort S with the merge-sort algorithm? What about quick-sort?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    The exercise does not state whether the 0s and 1s are equally likely to
    appear in the sequence, but either way there will be many duplicate values.
    Merge-sort has a worst-case run time of O(nlogn), regardless of how many
    duplicates exists in the sequence.  It also cannot take advantage of "runs"
    in the data, and so I would expect merge-sort to require O(nlogn) time.

    As for quick-sort, each recursive call of quick-sort chooses
    a value from the sequence as a pivot, and splits the sequence into
    sub-sequences of values that are either greater than, less than, or equal
    to the pivot value.  But with the elements of the sequence restricted to
    two values, the pivot can never be the median value of the sequence.
    A pivot value that is consistently close to the median of the sequence is
    typically the ideal case to achieve O(nlogn) performance.

    Instead, the pivot will always be either 0 or 1, and the values in the
    sequence will either all be stored in L and E, or all stored in G and E.
    There are two scenarios that could ensue:

    1. The distribution of 0s and 1s in the sequence are roughly equal
    2. The distribution of 0s and 1s is skewed towards either 0 or 1

    If the sequence is composed of a roughly equal number of 0s and 1s, then
    each recursive call of quick-sort will split the sequence roughly in half:
    half of the elements in E, and the other half in (one of) L or G.  This
    halving of the length of the sequence will result in a quick-sort binary
    tree of height log(n), and so the run-time efficiency of quick-sort would
    thus be O(nlogn).

    If the distribution is skewed towards mostly 0s or mostly 1s, then each
    recursive call of quick-sort will place the majority of values in either E
    or (one of) L or G.  If the sequence is mostly 0s (for instance), most of
    the time the pivot will be a zero and most of the values will go to E.
    Very few values will go to G, and so the size of the sequence will be
    quickly reduced.  In the extreme, if the entire sequence was 0s with no 1s,
    then all of the value would be placed in E and quick-sort would return
    after a single call as L and G are empty.  This corresponds to a
    quick-sort binary tree of height 1, and so the expected run-time is O(n).

    As a final answer, under this scenario we would expect quick-sort's
    run-time efficiency to be bounded between Ω(n) and O(nlogn).
    """
    return True


def how_long_bucket_sort():
    """Solution to exercise R-12.20.

    Suppose S is a sequence of n values, each equal to 0 or 1. How long will
    it take to sort S stably with the bucket-sort algorithm?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    In this scenario N = 2, and all of the values will be inserted into either
    index 0 or index 1 of the bucket array.  Bucket-sort will stably sort the
    sequence regardless of the number of duplicates.

    The run-time efficiency of bucket-sort is O(n + N), and if N is small
    relative to n bucket-sort is O(n).

    A sequence of n < 2 is already sorted, and so it's safe to say that in this
    scenario bucket-sort's run-time efficiency is O(n).
    """
    return True


def inplace_sort(S):
    """Solution to exercise R-12.21.

    Given a sequence S of n values, each equal to 0 or 1, describe an in-place
    method for sorting S.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    I used a solution similar to the in-place quick-sort algorithm, except
    that the pivot is always be the same value and there is no need for
    recursion.

    The left cursor begins at the first element of S, and the right cursor at
    the last element of S.  If the element at the left cursor is zero, then the
    left cursor is incremented by 1.

    If the element at the left cursor is 1, then the element is swapped with
    the element at the right cursor, and the right cursor is decremented by 1.
    If the swapped element is still a 1, the element will keep getting swapped
    to the right cursor's position until a zero is found.

    In this way the two cursors approach each other until they meet.  At this
    point the sort is complete.  All indices less than the final cursor
    position will contain zeros, all indices greater than the final cursor
    position will contain ones, and the index of the final cursor position can
    contain either a 0 or 1 - it doesn't matter.

    Only a small additional amount of memory is used to store the left and
    right cursors, and so this sort algorithm is in-place.  Each loop uses O(1)
    operations and there will be n loops, and so the in-place sort is O(n).
    """
    left = 0
    right = len(S)-1
    while left < right:
        if S[left] == 1:
            S[left], S[right] = S[right], S[left]
            right -= 1
        else:
            left += 1


def insertion_sort():
    """Solution to exercise R-12.22.

    Give an example input list that requires merge-sort and heap-sort to take
    O(n log n) time to sort, but insertion-sort runs in O(n) time. What if you
    reverse this list?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Insertion-sort runs in O(n) time when the sequence is already sorted, such
    as [0, 1, 2, 3, 4, 5].  This is because the inner loop of the insertion-
    sort never needs to run, and the outer loop runs for n iterations.

    Merge-sort is guaranteed to run in worst-case O(nlogn) time regardless of
    whether the list is sorted.  The fact that the list is already sorted does
    not improve its run-time, because it will recursively split the sequence
    in halves even if it is already sorted.

    Heap-sort's run-time efficiency is tied to the height of the heap.  As
    items are added to the heap they will have to be "up-heap bubbled" in order
    to preserve the heap-order and complete binary tree properties.  This
    requires O(nlogn) time as each added item i requires O(logi) time to move
    up the tree.  However, if a heap is constructed from a sorted list each
    added element should preserve the heap-order and completeness properties.
    This will reduce the phase 1 run-time to O(n).  But in order to sort the
    list, the remove_min() method must be called n times.  Each time
    remove_min() is called, the root of the heap is replaced by a value from
    the bottom of the heap.  This value must then be "down-heap bubbled" which
    will require time proportional to the height of the tree.  Thus the phase 2
    run-time of heap-sort is O(nlogn), making the overall run-time efficiency
    of heap-sort O(nlogn) even for an already sorted list.

    If the sorted list is reversed, then insertion-sort runs in O(n^2) time
    because the inner loop must perform 0, 1, 2, ..., n-1 swaps.  This is the
    sum of the first n integers, hence the O(n^2) run-time.  Merge-sort and
    heap-sort will still sort the reversed list in O(nlogn) time.
    """
    return True


def best_algorithm():
    """Solution to exercise R-12.23.

    What is the best algorithm for sorting each of the following: general com-
    parable objects, long character strings, 32-bit integers, double-precision
    floating-point numbers, and bytes? Justify your answer.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    1. General comparable objects:
        a. If the sequence is small-to-medium-sized, heap-sort is guaranteed to
           be O(nlogn) worst-case.

        b. If the sequence is large and memory is not an issue, merge-sort is
           worst-case O(nlogn) and may outperform heap-sort.

        c. If the sequence is large and memory usage is an issue, quick-sort
           can easily run in-place and may outperform both heap-sort and
           quick-sort with its expected O(nlogn) run-time efficiency.  However,
           worst-case it is O(n^2), and this may not be acceptable for real-
           time applications.

        d. Insertion-sort, radix-sort, bucket-sort:
           Bucket-sort and radix-sort require sequences of integers, and so in
           general can't be recommended.  Insertion-sort performs well on small
           sequences - especially if they are already nearly sorted.  Again,
           this is a special case and in general insertion-sort can't be
           recommended.

    2. Long character strings:
        a. Radix-sort is ideal for character strings, because it will perform a
           lexicographic sort of the strings in O(d(n + N)) time.  If the
           strings are long d might be quite large, but even so other sorting
           methods will not lexicographically sort strings without
           modification.

        b. Quick-sort and heap-sort are not stable sorting methods, and so
           cannot lexicographically sort a string.

        c. Merge-sort is a stable sorting algorithm, and so if d is large
           enough it may be worth modifying merge-sort to handle strings.

    3. 32-bit integers:
        a. If the integers happen to be constrained to a range N that is O(n),
           then the best sorting algorithm is bucket-sort, because bucket-sort
           can sort integers in O(n) time.

        b. If the integers are not constrained to a range N that is O(n) and
           are quite large compared to n, then another sorting method will
           provide better results.  In this case, the same recommendations
           for general comparable objects will apply.

    4. Double-precision floating-point numbers
       a. The same recommendations for general comparable objects apply here.


    5. Bytes
        a. It's possible to represent a byte as a d-tuple of d bits, each bit
           being either 0 or 1.  In this case N = 2, and so radix-sort should
           run in O(n) time.

        b. Bytes can be represented as integers, and so a bucket-sort may be
           appropriate if N is constrained to be O(n).
    """
    return True


def quick_select():
    """Solution to exercise R-12.24.

    Show that the worst-case running time of quick-select on an n-element
    sequence is Ω(n^2).

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    In the worst case, the randomly selected pivot value will always be the
    maximum value of the sequence when searching for the minimum value,
    or the pivot will always be the minimum value of the sequence when
    searching for the maximum value.  This will result in all of the
    sequence values being placed in either the L or G list, and the length of
    the sequence will only reduce by one per recursive call to quick-select.
    The algorithm will then run n, n-1, n-2, n-3, ..., 1 comparisons,
    which is the sum of the first n integers and is equal to n(n+1)/2.  In this
    worst-case scenario the lower bound on run-time efficiency is thus Ω(n^2).
    """
    return True
