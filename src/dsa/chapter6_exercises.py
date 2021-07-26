#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 6 exercises.

###############################################################################
# chapter6_exercises.py
#
# Revision:     1.00
# Date:         6/30/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 6 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports
from collections import deque

# Related third party imports

# Local application/library specific imports


# %% Source code from text, hosted at https://github.com/mjwestcott/Goodrich
class Empty(Exception):
    """Error attempting to access an element from an empty container."""


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""

    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):                 # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                    # keep track of existing list
        # allocate list with new capacity
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):         # only consider existing elements
            self._data[k] = old[walk]       # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size as modulus
        self._front = 0                     # front has been realigned


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []                       # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)                  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list

    def pop(self):
        """Remove and return the element from top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               # remove last item from list


# %% Reinforcement Exercises
def stack_operations():
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
    values = [
        [],
        [5],
        [5, 3],
        [5],
        [5, 2],
        [5, 2, 8],
        [5, 2],
        [5],
        [5, 9],
        [5, 9, 1],
        [5, 9],
        [5, 9, 7],
        [5, 9, 7, 6],
        [5, 9, 7],
        [5, 9],
        [5, 9, 4],
        [5, 9],
        [5]
    ]
    return values


def stack_operations2():
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
    return 18


def transfer(S, T):
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
    for _ in range(len(S)):
        T.push(S.pop())


def reverse_list(alist):
    """Solution to exercise R-6.5.

    Implement a function that reverses a list of elements by pushing them onto
    a stack in one order, and writing them back to the list in reversed order.
    """
    stack = ArrayStack()
    for x in alist:
        stack.push(x)
    for idx in range(len(stack)):
        alist[idx] = stack.pop()


def queue_operations():
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
    values = [
        [],
        [5],
        [5, 3],
        [3],
        [3, 2],
        [3, 2, 8],
        [2, 8],
        [8],
        [8, 9],
        [8, 9, 1],
        [9, 1],
        [9, 1, 7],
        [9, 1, 7, 6],
        [1, 7, 6],
        [7, 6],
        [7, 6, 4],
        [6, 4],
        [4]
    ]
    return values


def queue_operations2():
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
    return 22


def queue_operations3():
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
    return 10


class DequeQueue:
    """Solution to exercise R-6.11.

    FIFO queue implementation using a deque as underlying storage.
    """

    def __init__(self):
        """Create an empty queue."""
        self._data = deque()

    def __len__(self):
        """Return the number of elements in the queue."""
        return len(self._data)

    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._data) == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data.popleft()

    def enqueue(self, e):
        """Add an element to the back of queue."""
        self._data.append(e)


def deque_ops():
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
    return [
        ('None', None, []),
        ('add_first()', 4, [4]),
        ('add_last()', 8, [4, 8]),
        ('add_last()', 9, [4, 8, 9]),
        ('add_first()', 5, [5, 4, 8, 9]),
        ('last()', 9, [5, 4, 8, 9]),
        ('delete_first()', 5, [4, 8, 9]),
        ('delete_last()', 9, [4, 8]),
        ('add_last()', 7, [4, 8, 7]),
        ('first()', 4, [4, 8, 7]),
        ('last()', 7, [4, 8, 7]),
        ('add_last()', 6, [4, 8, 7, 6]),
        ('delete_first()', 4, [8, 7, 6]),
        ('delete_first()', 8, [7, 6])
    ]


def deque_and_queue():
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
    deq = deque([1, 2, 3, 4, 5, 6, 7, 8])
    queue = ArrayQueue()
    for _ in range(8):
        queue.enqueue(deq.popleft())        # Step 1
    for _ in range(3):
        deq.append(queue.dequeue())         # Step 2
    deq.appendleft(queue.dequeue())         # Step 3
    deq.append(queue.dequeue())             # Step 4
    deq.append(deq.popleft())               # Step 5
    for _ in range(3):
        deq.append(queue.dequeue())         # Step 6
    return deq, queue


def deque_and_stack():
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
    deq = deque([1, 2, 3, 4, 5, 6, 7, 8])
    stack = ArrayStack()
    for _ in range(4):
        stack.push(deq.pop())       # Step 1
    deq.appendleft(deq.pop())       # Step 2
    deq.append(stack.pop())         # Step 3
    deq.append(deq.popleft())       # Step 4
    for _ in range(3):
        deq.append(stack.pop())     # Step 5
    return deq, stack


# %% Creativity Exercises
def stack_search(x, deq, stack):
    """Solution to exercise C-6.27.

    Suppose you have a stack S containing n elements and a queue Q that is
    initially empty. Describe how you can use Q to scan S to see if it
    contains a certain element x, with the additional constraint that your
    algorithm must return the elements back to S in their original order. You
    may only use S, Q, and a constant number of other variables.
    """
    x_found = False
    for _ in range(len(stack)):
        deq.append(stack.pop())
        if deq[-1] == x:
            x_found = True
    for _ in range(len(deq)):
        stack.push(deq.pop())  # Put elements back in original order
    return x_found


class RotateQueue:
    """Solution to exercise C-6.29.

    FIFO queue implementation using a Python list as underlying storage.
    Implements additional rotate() method to dequeue and then enqueue a value.
    """

    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):                 # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                    # keep track of existing list
        # allocate list with new capacity
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):         # only consider existing elements
            self._data[k] = old[walk]       # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size as modulus
        self._front = 0                     # front has been realigned

    def rotate(self):
        """Rotate the element at the front of the queue to the back.

        Return the element at the front of the queue, and then immediately
        enqueue the element at the back of the queue.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # Replace value to be dequeued
        # Find index of next available slot in queue
        avail = (self._front + self._size) % len(self._data)
        # Increment the front of the queue by one position
        self._front = (self._front + 1) % len(self._data)
        # Place the (former) front value at the back of the queue
        self._data[avail] = answer
        return answer  # Return the (former) front value of the queue


def cow_bridge():
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
    cows = {
        'Mazie': 2,
        'Daisy': 4,
        'Crazy': 10,
        'Lazy': 20
    }
    # Step 0, initial state
    yoke = ArrayStack()
    time = 0
    start = [cow for cow in cows.keys()]
    across_bridge = []
    # Step 1, Mazie and Daisy cross bridge, only Mazie stays
    yoke.push(start.pop(start.index('Daisy')))      # Daisy in yoke
    yoke.push(start.pop(start.index('Mazie')))      # Mazie in yoke
    across_bridge.append(yoke.pop())                # Mazie out of yoke
    time += max(cows['Daisy'], cows['Mazie'])
    # Step 2, Daisy walks back to start by itself
    start.append(yoke.pop())                        # Daisy back at start
    time += cows['Daisy']
    # Step 3, Crazy and Lazy walk across bridge
    yoke.push(start.pop(start.index('Crazy')))      # Crazy in yoke
    yoke.push(start.pop(start.index('Lazy')))       # Lazy in yoke
    across_bridge.append(yoke.pop())                # Lazy out of yoke
    across_bridge.append(yoke.pop())                # Crazy out of yoke
    time += max(cows['Crazy'], cows['Lazy'])
    # Step 4, Mazie walks back to start by itself
    yoke.push(across_bridge.pop(across_bridge.index('Mazie')))  # Mazie in yoke
    time += cows['Mazie']
    # Step 5, Mazie and Daisy cross the bridge
    yoke.push(start.pop(start.index('Daisy')))      # Daisy in yoke
    across_bridge.append(yoke.pop())                # Daisy out of yoke
    across_bridge.append(yoke.pop())                # Mazie out of yoke
    time += max(cows['Daisy'], cows['Mazie'])
    return time, start, across_bridge


# %% Project Exercises
class ArrayDeque:
    """Solution to exercise P-6.32.

    Give a complete ArrayDeque implementation of the double-ended queue
    ADT as sketched in Section 6.3.2.
    """

    DEFAULT_CAPACITY = 10  # Capacity for new deques

    def __init__(self):
        """Create an empty deque."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the element at the back of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[self._back]

    def delete_first(self):
        """Remove and return the first element of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None      # help garbage collection
        self._size -= 1
        if self._size > 0:  # If last item removed front does not move
            self._front = (self._front + 1) % len(self._data)
        return answer

    def delete_last(self):
        """Remove and return the last element of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._back]
        self._data[self._back] = None      # help garbage collection
        self._size -= 1
        if self._size > 0:  # If last item removed back does not move
            self._back = (self._back - 1) % len(self._data)
        return answer

    def add_first(self, e):
        """Add an element to the front of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        if self.is_empty():
            self._data[self._front] = e
        else:
            self._front = (self._front - 1) % len(self._data)
            self._data[self._front] = e
        self._size += 1

    def add_last(self, e):
        """Add an element to the back of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        if self.is_empty():
            self._data[self._back] = e
        else:
            self._back = (self._back + 1) % len(self._data)
            self._data[self._back] = e
        self._size += 1

    def _resize(self, cap):                 # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data                    # keep track of existing list
        # allocate list with new capacity
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):         # only consider existing elements
            self._data[k] = old[walk]       # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size as modulus
        self._front = 0                     # front has been realigned
        self._back = self._size - 1


def postfix_notation(postfix):
    """Solution to exercise P-6.34.

    Implement a program that can input an expression in postfix notation (see
    Exercise C-6.22) and output its value.
    """
    ops = '+-*/'
    results = ArrayStack()
    for item in postfix:
        if item.isnumeric():
            results.push(float(item))
        elif item in ops:
            var2 = results.pop()
            var1 = results.pop()
            if item == '+':
                result = var1 + var2
            if item == '-':
                result = var1 - var2
            if item == '*':
                result = var1 * var2
            if item == '/':
                result = var1 / var2
            results.push(result)
    return results.pop()


class LeakyStack:
    """Solution to exercise P-6.35."""

    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty stack."""
        self._data = []                       # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        if len(self._data) == LeakyStack.DEFAULT_CAPACITY:
            self._leak()
            self._data[-1] = e                # new item stored at end of list
        else:
            self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list

    def pop(self):
        """Remove and return the element from top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               # remove last item from list

    def _leak(self):
        """Leak the oldest item from the stack.

        Shift all elements down one position in the stack, overwriting the
        oldest item.
        """
        for idx in range(1, LeakyStack.DEFAULT_CAPACITY):
            self._data[idx-1] = self._data[idx]
