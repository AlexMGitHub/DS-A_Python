#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test solutions to chapter 6 exercises.

###############################################################################
# test_chapter6.py
#
# Revision:     1.00
# Date:         6/30/2021
# Author:       Alex
#
# Purpose:      Runs unit tests on all chapter 6 exercises from "Data
#               Structures and Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports
from collections import deque

# Related third party imports
import pytest

# Local application/library specific imports
import dsa.chapter6_exercises as chap6


# %% Reinforcement Exercises
def test_stack_operations():
    """Solution to exercise R-6.1.

    What values are returned during the following series of stack operations,
    if executed upon an initially empty stack? push(5), push(3), pop(),
    push(2), push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6),
    pop(), pop(), push(4), pop(), pop().

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A stack is a last-in, first-out (LIFO) structure:
    1. Initial      []
    2. push(5)      [5]
    3. push(3)      [5, 3]
    4. pop()        [5]
    5, push(2)      [5, 2]
    6. push(8)      [5, 2, 8]
    7. pop()        [5, 2]
    8. pop()        [5]
    9. push(9)      [5, 9]
    10. push(1)     [5, 9, 1]
    11. pop()       [5, 9]
    12. push(7)     [5, 9, 7]
    13. push(6)     [5, 9, 7, 6]
    14. pop()       [5, 9, 7]
    15. pop()       [5, 9]
    16. push(4)     [5, 9, 4]
    17. pop()       [5, 9]
    18. pop()       [5]
    """
    operations = [
        None,
        ('push', 5),
        ('push', 3),
        ('pop'),
        ('push', 2),
        ('push', 8),
        ('pop'),
        ('pop'),
        ('push', 9),
        ('push', 1),
        ('pop'),
        ('push', 7),
        ('push', 6),
        ('pop'),
        ('pop'),
        ('push', 4),
        ('pop'),
        ('pop')
    ]
    values = chap6.stack_operations()  # My answers to the exercise
    # Instantiate a stack and perform the stack operations to verify my answers
    stack = chap6.ArrayStack()
    for value, op in zip(values, operations):
        if op is not None:
            if op[0] == 'push':
                stack.push(op[1])
            else:
                stack.pop()
        assert value == stack._data  # Test answer for every operation


def test_stack_operations2():
    """Solution to exercise R-6.2.

    Suppose an initially empty stack S has executed a total of 25 push opera-
    tions, 12 top operations, and 10 pop operations, 3 of which raised Empty
    errors that were caught and ignored. What is the current size of S?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. 25 push operations increase the size of the stack to:        25
    2. 12 top operations have no effect on the size of the stack:   25
    3. 10 pop operations reduce the size of the stack by 10:        15
    4. However, 3 of them raised Empty errors, and so did nothing:  18

    The total size of the stack is 18 elements.
    """
    stack = chap6.ArrayStack()
    for x in range(3):
        with pytest.raises(chap6.Empty):
            stack.pop()
    for x in range(25):
        stack.push(x)
    for x in range(12):
        stack.top()
    for x in range(7):
        stack.pop()
    assert chap6.stack_operations2() == len(stack)


def test_transfer():
    """Solution to exercise R-6.3.

    Implement a function with signature transfer(S, T) that transfers all ele-
    ments from stack S onto stack T, so that the element that starts at the top
    of S is the first to be inserted onto T, and the element at the bottom of S
    ends up at the top of T.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    S will pop all n of its values in LIFO order (reverse order).
    T will push all n elements from S into its stack.
    The transfer can be verified by popping n elements from T, which will be
    reversed in order a second time.  This results in the original sequence of
    values stored in S.
    """
    stack1 = chap6.ArrayStack()
    stack2 = chap6.ArrayStack()
    n = 10
    for x in range(n):
        stack1.push(x)
    chap6.transfer(stack1, stack2)
    assert len(stack1) == 0
    assert len(stack2) == n
    for expected in range(n):
        assert stack2.pop() == expected


def test_reverse_list():
    """Solution to exercise R-6.5.

    Implement a function that reverses a list of elements by pushing them onto
    a stack in one order, and writing them back to the list in reversed order.
    """
    n = 10
    alist = list(range(n))
    chap6.reverse_list(alist)
    assert alist == list(range(n-1, -1, -1))


@pytest.fixture(name="queue_ops", scope="function")
def queue_fixture():
    """Fixture to supply operations for the ArrayQueue() class."""

    class QueueOps:
        """Fixture class to store queue operations."""

        def __init__(self):
            """Operations to be used for testing the ArrayQueue() class."""
            self.operations = [
                None,
                ('enqueue', 5),
                ('enqueue', 3),
                ('dequeue'),
                ('enqueue', 2),
                ('enqueue', 8),
                ('dequeue'),
                ('dequeue'),
                ('enqueue', 9),
                ('enqueue', 1),
                ('dequeue'),
                ('enqueue', 7),
                ('enqueue', 6),
                ('dequeue'),
                ('dequeue'),
                ('enqueue', 4),
                ('dequeue'),
                ('dequeue')
            ]
    return QueueOps()


def test_queue_operations(queue_ops):
    """Solution to exercise R-6.7.

    What values are returned during the following sequence of queue opera-
    tions, if executed on an initially empty queue? enqueue(5), enqueue(3),
    dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9),
    enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(),
    enqueue(4), dequeue(), dequeue().

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A queue is a first-in, first-out (FIFO) structure:
    1. Initial         []
    2. enqueue(5)      [5]
    3. enqueue(3)      [5, 3]
    4. dequeue()       [3]
    5, enqueue(2)      [3, 2]
    6. enqueue(8)      [3, 2, 8]
    7. dequeue()       [2, 8]
    8. dequeue()       [8]
    9. enqueue(9)      [8, 9]
    10. enqueue(1)     [8, 9, 1]
    11. dequeue()      [9, 1]
    12. enqueue(7)     [9, 1, 7]
    13. enqueue(6)     [9, 1, 7, 6]
    14. dequeue()      [1, 7, 6]
    15. dequeue()      [7, 6]
    16. enqueue(4)     [7, 6, 4]
    17. dequeue()      [6, 4]
    18. dequeue()      [4]
    """
    operations = queue_ops.operations  # Queue operations stored in fixture
    values = chap6.queue_operations()  # My answers to the exercise
    # Instantiate a queue and perform the queue operations to verify my answers
    queue = chap6.ArrayQueue()
    for value, op in zip(values, operations):
        if op is not None:
            if op[0] == 'enqueue':
                queue.enqueue(op[1])
            else:
                queue.dequeue()
        # Use circular indexing to access elements in queue
        cap = len(queue._data)
        indices = [(queue._front + x) % cap for x in range(len(queue))]
        queue_vals = [queue._data[idx] for idx in indices]
        assert value == queue_vals  # Test answer for every operation


def test_queue_operations2():
    """Solution to exercise R-6.8.

    Suppose an initially empty queue Q has executed a total of 32 enqueue
    operations, 10 first operations, and 15 dequeue operations, 5 of which
    raised Empty errors that were caught and ignored. What is the current
    size of Q?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. 32 enqueue operations increase the size of the stack to:         32
    2. 10 first operations have no effect on queue size:                32
    3. 15 dequeue operations reduce the size of the stack by 15:        17
    4. However, 5 of them raised Empty errors, and so did nothing:      22

    The current size of the queue is 22 elements.
    """
    queue = chap6.ArrayQueue()
    for x in range(5):
        with pytest.raises(chap6.Empty):
            queue.dequeue()
    for x in range(32):
        queue.enqueue(x)
    for x in range(10):
        queue.first()
    for x in range(10):
        queue.dequeue()
    assert chap6.queue_operations2() == len(queue)


def test_queue_operations3():
    """Solution to exercise R-6.9.

    Had the queue of the previous problem been an instance of ArrayQueue
    that used an initial array of capacity 30, and had its size never been
    greater than 30, what would be the final value of the front instance
    variable?

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    1. 5 dequeue operations on empty queue do not move front from 0
    2. 30 consecutive queue operations do not move front from 0
    3. 10 dequeue operations move front of queue to 10
    4. 10 first operations do not move front of queue from 10
    5. 2 queue operations (total 32) do not move front of queue from 10

    The front of the queue is at position 10.
    """
    chap6.ArrayQueue.DEFAULT_CAPACITY = 30
    queue = chap6.ArrayQueue()
    for x in range(5):
        with pytest.raises(chap6.Empty):
            queue.dequeue()
    for x in range(30):
        queue.enqueue(x)
    for x in range(10):
        queue.dequeue()
    for x in range(10):
        queue.first()
    for x in range(2):
        queue.enqueue(x)
    assert queue._front == chap6.queue_operations3()
    chap6.ArrayQueue.DEFAULT_CAPACITY = 10  # Reset default capacity


def test_deque_queue(queue_ops):
    """Solution to exercise R-6.11.

    Give a simple adapter that implements our queue ADT while using a
    collections.deque instance for storage.
    """
    operations = queue_ops.operations   # Queue operations stored in fixture
    deque_q = chap6.DequeQueue()        # Queue based on deque
    queue = chap6.ArrayQueue()          # Queue based on list
    # Perform queue operations and verify results agree between the queues
    for op in operations:
        if op is not None:
            if op[0] == 'enqueue':
                queue.enqueue(op[1])
                deque_q.enqueue(op[1])
            else:
                queue.dequeue()
                deque_q.dequeue()
        # Use circular indexing to access elements in queue
        cap = len(queue._data)
        indices = [(queue._front + x) % cap for x in range(len(queue))]
        queue_vals = [queue._data[idx] for idx in indices]
        deque_q_vals = list(deque_q._data)
        assert deque_q_vals == queue_vals  # Compare queues for every operation


def test_deque_ops():
    """Solution to exercise R-6.12.

    What values are returned during the following sequence of deque ADT op-
    erations, on initially empty deque? add first(4), add last(8), add last(9),
    add first(5), back( ), delete first( ), delete last( ), add last(7),
    first( ), last( ), add last(6), delete first( ), delete first( ).

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    A deque can add or remove items from either end of the queue:
    1. Initial              []
    2. add_first(4)         [4]
    3. add_last(8)          [4, 8]
    4. add_last(9)          [4, 8, 9]
    5. add_first(5)         [5, 4, 8, 9]
    6. last()               9
    7. delete_first()       5, [4, 8, 9]
    8. delete_last()        9, [4, 8]
    9. add_last(7)          [4, 8, 7]
    10. first()             4
    11. last()              7
    12. add_last(6)         [4, 8, 7, 6]
    13. delete_first()      4, [8, 7, 6]
    14. delete_first()      8, [7, 6]
    """
    operations = chap6.deque_ops()
    deq = deque()
    for op in operations:
        if op[0] == 'add_first()':
            deq.appendleft(op[1])
        elif op[0] == 'add_last()':
            deq.append(op[1])
        elif op[0] == 'first':
            assert deq[0] == op[1]
        elif op[0] == 'last()':
            assert deq[-1] == op[1]
        elif op[0] == 'delete_first()':
            assert deq.popleft() == op[1]
        elif op[0] == 'delete_last()':
            assert deq.pop() == op[1]
        assert list(deq) == op[2]  # Verify state of deque after every op


def test_deque_and_queue():
    """Solution to exercise R-6.13.

    Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8),
    in this order. Suppose further that you have an initially empty queue Q.
    Give a code fragment that uses only D and Q (and no other variables) and
    results in D storing the elements in the order (1, 2, 3, 5, 4, 6, 7, 8).

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    0. Initial state                    Deque [1, 2, 3, 4, 5, 6, 7, 8]
                                        Queue []

    1. popleft() all nums from          Deque []
       D to Q                           Queue [1, 2, 3, 4, 5, 6, 7, 8]

    2. addright() 3 nums to D           Deque [1, 2, 3]
       from Q                           Queue [4, 5, 6, 7, 8]

    3. addleft() 1 num to D             Deque [4, 1, 2, 3]
       from Q                           Queue [5, 6, 7, 8]

    4. addright() 1 num to D            Deque [4, 1, 2, 3, 5]
       from Q                           Queue [6, 7, 8]

    5. popleft() 1 num from D,          Deque [1, 2, 3, 5, 4]
       addright() that num to D         Queue [6, 7, 8]

    6. addright() 3 nums to D           Deque [1, 2, 3, 5, 4, 6, 7, 8]
       from Q                           Queue []
    """
    deq, queue = chap6.deque_and_queue()
    assert len(queue) == 0
    assert list(deq) == [1, 2, 3, 5, 4, 6, 7, 8]


def test_deque_and_stack():
    """Solution to exercise R-6.14.

    Repeat the previous problem using the deque D and an initially empty
    stack S.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    0. Initial state                    Deque [1, 2, 3, 4, 5, 6, 7, 8]
                                        Stack []

    1. popright() 4 nums to S           Deque [1, 2, 3, 4]
       from D                           Stack [8, 7, 6, 5]

    2. popright() 1 num from D,         Deque [4, 1, 2, 3]
       addleft() that num to D          Stack [8, 7, 6, 5]

    3. addright() 1 nums to D           Deque [4, 1, 2, 3, 5]
       from S                           Stack [8, 7, 6]

    4. popleft() 1 num from D,          Deque [1, 2, 3, 5, 4]
       addright() that num to D         Stack [8, 7, 6]

    5. addright() 3 nums to D           Deque [1, 2, 3, 5, 4, 6, 7, 8]
       from S                           Stack []
    """
    deq, stack = chap6.deque_and_stack()
    assert len(stack) == 0
    assert list(deq) == [1, 2, 3, 5, 4, 6, 7, 8]


# %% Creativity Exercises
def test_stack_search():
    """Solution to exercise C-6.27.

    Suppose you have a stack S containing n elements and a queue Q that is
    initially empty. Describe how you can use Q to scan S to see if it
    contains a certain element x, with the additional constraint that your
    algorithm must return the elements back to S in their original order. You
    may only use S, Q, and a constant number of other variables.
    """
    stack = chap6.ArrayStack()
    for x in range(10):
        stack.push(x)
    deq = deque()
    x_found = chap6.stack_search(5, deq, stack)
    assert x_found                          # 5 is in the stack
    assert len(deq) == 0                    # Verify deque is empty
    assert stack._data == list(range(10))   # Verify original stack order
    x_found = chap6.stack_search(11, deq, stack)
    assert not x_found                      # 11 is not in the stack
    assert len(deq) == 0                    # Verify deque is empty
    assert stack._data == list(range(10))   # Verify original stack order


@pytest.mark.parametrize('n', [5, 10, 20])
def test_queue_rotate(n):
    """Solution to exercise C-6.29.

    In certain applications of the queue ADT, it is common to repeatedly
    dequeue an element, process it in some way, and then immediately en-
    queue the same element. Modify the ArrayQueue implementation to in-
    clude a rotate( ) method that has semantics identical to the combina-
    tion, Q.enqueue(Q.dequeue( )). However, your implementation should
    be more efficient than making two separate calls (for example, because
    there is no need to modify size).
    """
    queue = chap6.ArrayQueue()       # Original queue class
    r_que = chap6.RotateQueue()      # Queue class with new rotate() method
    for x in range(n):               # Enqueue queues with same data
        queue.enqueue(x)
        r_que.enqueue(x)
    for _ in range(2*len(queue)):    # Rotate thru values in both queues twice
        queue.enqueue(queue.dequeue())
        r_que.rotate()
        assert queue._data == r_que._data  # Verify operations are equivalent
        assert queue._front == r_que._front


def test_cow_bridge():
    """Solution to exercise C-6.31.

    Suppose Bob has four cows that he wants to take across a bridge, but only
    one yoke, which can hold up to two cows, side by side, tied to the yoke.
    The yoke is too heavy for him to carry across the bridge, but he can tie
    (and untie) cows to it in no time at all. Of his four cows, Mazie can cross
    the bridge in 2 minutes, Daisy can cross it in 4 minutes, Crazy can cross
    it in 10 minutes, and Lazy can cross it in 20 minutes. Of course, when
    two cows are tied to the yoke, they must go at the speed of the slower cow.
    Describe how Bob can get all his cows across the bridge in 34 minutes.

    --------------------------------------------------------------------------
    Solution:
    --------------------------------------------------------------------------
    The solution is described below, where:
        #() == Yoke
        M2  == Mazie (2  minutes)
        D4  == Daisy (4  minutes)
        C10 == Crazy (10 minutes)
        L20 == Lazy  (20 minutes)

    0. Initial state          # M2, D4, |======|
                              C10, L20  |======|                0  mins

    1. #(D4, M2)   -->        C10, L20  |======| #(D4, M2)
                                        |======|                4  mins

    2. #(  , D4)   <--       # D4, C10, |======|   M2
                                   L20  |======|                8  mins

    3. #(C10, L20) -->              D4  |======|   M2,
                                        |======| #(C10, L20)    28 mins

    4. #(  , M2)   <--        # M2, D4  |======|   C10, L20
                                        |======|                30 mins

    5. #(M2, D4)   -->                  |======| #(M2, D4),
                                        |======|   C10, L20     34 mins

    The yoke can be implemented as a stack containing a maximum of 2 elements.
    """
    time, start, across_bridge = chap6.cow_bridge()
    assert len(start) == 0
    assert len(across_bridge) == 4
    assert time == 34


# %% Project Exercises
def test_array_deque():
    """Solution to exercise P-6.32.

    Give a complete ArrayDeque implementation of the double-ended queue
    ADT as sketched in Section 6.3.2.
    """
    n = 30                      # Maximum number of elements to add to deque
    deq = deque()               # Collections deque
    adeq = chap6.ArrayDeque()   # The ArrayDeque() class to be tested
    # Test add_last() method as well as first(), last(), len() methods
    for x in range(n//2):
        deq.append(x)
        adeq.add_last(x)
        assert deq[0] == adeq.first()
        assert deq[-1] == adeq.last()
        assert len(deq) == len(adeq)
    # Test add_first() method as well as first(), last(), len() methods
    for x in range(n//2):
        deq.appendleft(x)
        adeq.add_first(x)
        assert deq[0] == adeq.first()
        assert deq[-1] == adeq.last()
        assert len(deq) == len(adeq)
    # Test delete_last() method as well as first(), last(), len() methods
    for _ in range(n//2):
        deq.pop()
        adeq.delete_last()
        assert deq[0] == adeq.first()
        assert deq[-1] == adeq.last()
        assert len(deq) == len(adeq)
    # Test delete_first() method as well as first(), last(), len() methods
    for _ in range(n//2+1):
        if len(deq) >= 2:
            deq.popleft()
            adeq.delete_first()
            assert deq[0] == adeq.first()
            assert deq[-1] == adeq.last()
            assert len(deq) == len(adeq)
        elif len(deq) == 1:
            deq.popleft()         # Pop last element
            adeq.delete_first()
        elif len(deq) == 0:
            assert len(deq) == len(adeq)
            # Verify removing from an empty list raises error
            with pytest.raises(IndexError):
                deq.popleft()
            with pytest.raises(chap6.Empty):
                adeq.delete_first()
            # Verify viewing elements in empty list raises error
            with pytest.raises(chap6.Empty):
                adeq.first()
            with pytest.raises(chap6.Empty):
                adeq.last()
            with pytest.raises(IndexError):
                deq[0]
            with pytest.raises(IndexError):
                deq[-1]


def test_postfix_notation():
    """Solution to exercise P-6.34.

    Implement a program that can input an expression in postfix notation (see
    Exercise C-6.22) and output its value.
    """
    infix = ((5 + 2) * (8 - 3)) / 4
    postfix = '5 2 + 8 3 - * 4 /'
    postfix = list(postfix.replace(' ', ''))
    assert chap6.postfix_notation(postfix) == infix


def test_leaky_stack():
    """Solution to exercise P-6.35.

    When push is invoked with the stack at full capacity,
    rather than throwing a Full exception (as described in Exercise C-6.16),
    a more typical semantic is to accept the pushed element at the top while
    “leaking” the oldest element from the bottom of the stack to make room.
    Give an implementation of such a LeakyStack abstraction, using a circular
    array with appropriate storage capacity.
    """
    stack = chap6.LeakyStack()
    n = stack.DEFAULT_CAPACITY
    for x in range(3*n):
        stack.push(x)  # Verify old values are leaking as new values pushed
        assert stack._data == list(range(max(0, x+1-n), x+1))
    for x in range(n-1, -1, -1):
        stack.pop()  # Verify stack shrinks from full capacity
        assert len(stack) == x
        assert stack._data == list(range(2*n, 2*n+x))
    with pytest.raises(chap6.Empty):
        stack.pop()  # Empty stack should raise error when popped
