#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Solutions to chapter 13 exercises.

###############################################################################
# chapter13_exercises.py
#
# Revision:     1.00
# Date:         7/15/2021
# Author:       Alex
#
# Purpose:      Solutions to chapter 13 exercises from "Data Structures and
#               Algorithms in Python" by Goodrich et. al.
#
###############################################################################
"""

# %% Imports
# Standard system imports

# Related third party imports

# Local application/library specific imports
from textbook_src.ch13.find_kmp import compute_kmp_fail
from textbook_src.ch13.matrix_chain import matrix_chain


# %% Reinforcement Exercises
def prefixes_and_suffixes(P):
    """Solution to exercise R-13.1.

    List the prefixes of the string P ="aaabbaaa" that are also suffixes of P.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    For a string S of length n:
    1. A prefix is a substring of S of the form S[0:k] for 0 <= k <= n.
    2. A suffix is a substring of S of the form S[j:n] for 0 <= j <= n.

    The string P has length n = 8, and thus will have n + 1 suffixes and
    prefixes.  The '' symbol represents the null string of length 0.

    The prefixes of P for all valid values of k are:
    k =  0, 1,  2,   3,    4,     5,      6,       7,        8
        '', a, aa, aaa, aaab, aaabb, aaabba, aaabbaa, aaabbaaa

    The suffixes of P for all valid values of j are:
    j =         0,       1,      2,     3,    4,   5,  6, 7,  8
         aaabbaaa, aabbaaa, abbaaa, bbaaa, baaa, aaa, aa, a, ''

    The substrings in common are:
    '', a, aa, aaa, aaabbaaa
    """
    n = len(P)
    prefixes = set()
    suffixes = set()
    for idx in range(n+1):
        prefixes.add(P[0:idx])
        suffixes.add(P[idx:n+1])
    return prefixes & suffixes  # Return union of prefixes and suffixes


def longest_proper_prefix(P):
    """Solution to exercise R-13.2.

    What is the longest (proper) prefix of the string "cgtacgttcgtacg" that
    is also a suffix of this string?

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    For a string S of length n:
    1. A prefix is a substring of S of the form S[0:k] for 0 <= k <= n.
    2. A suffix is a substring of S of the form S[j:n] for 0 <= j <= n.

    A proper prefix of a string is a prefix that is not equal to the string
    itself; S[0:k] for 0 <= k < n.

    The string "cgtacgttcgtacg" has length n = 14, and thus will have n + 1
    suffixes and n proper prefixes.  The '' symbol represents the null string
    of length 0.

    The proper prefixes of P for all valid values of k are:
    k =  0, 1,  2,   3,    4,     5,      6,       7,        8,         9,
        '', c, cg, cgt, cgta, cgtac, cgtacg, cgtacgt, cgtacgtt, cgtacgttc,

                10,          11,           12,            13
        cgtacgttcg, cgtacgttcgt, cgtacgttcgta, cgtacgttcgtac

    The suffixes of P for all valid values of j are:
    j =              0,             1,            2,           3,          4,
        cgtacgttcgtacg, cgtacgttcgtac, cgtacgttcgta, cgtacgttcgt, cgtacgttcg,

                5,        6,       7,      8,     9,   10,  11, 12, 13, 14
        cgtacgttc, cgtacgtt, cgtacgt, cgtacg, cgtac, cgta, cgt, cg,  t, ''


    The longest common substring is "cgtacgttcgtac", which is 13 characters
    long.
    """
    n = len(P)
    prefixes = set()
    suffixes = set()
    for k in range(n):
        prefixes.add(P[0:k])        # Only proper prefixes k < n
    for j in range(n+1):
        suffixes.add(P[j:n+1])      # No restrictions on suffixes, j <= n
    common = prefixes & suffixes
    return max(common, key=len)     # Longest common prefix and suffix string


def draw_brute_force():
    """Solution to exercise R-13.3.

    Draw a figure illustrating the comparisons done by brute-force pattern
    matching for the text "aaabaadaabaaa" and pattern "aabaaa".

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Text:       aaabaadaabaaa
                123
    Pattern:    aabaaa                  # Mismatch, shift 1 character right

                aaabaadaabaaa
                 456789
                 aabaaa

                aaabaadaabaaa
                  01
                  aabaaa

                aaabaadaabaaa
                  23
                  aabaaa

                aaabaadaabaaa
                   4
                   aabaaa

                aaabaadaabaaa
                    567
                    aabaaa

                aaabaadaabaaa
                     89
                     aabaaa

                aaabaadaabaaa
                      0
                      aabaaa

                aaabaadaabaaa
                       123456
                       aabaaa           # Pattern matched

    The brute-force method performs 26 comparisons before finding a match for
    the pattern.
    """
    return True


def draw_boyer_moore():
    """Solution to exercise R-13.4.

    Repeat the previous problem for the Boyer-Moore algorithm, not counting
    the comparisons made to compute the last(c) function.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------

         c     |  a  b   d
    -----------|-----------
      last(c)  |  5  2  -1

    Text:       aaabaadaabaaa           # k = 3, j = last(b) = 2
                   321                  # Shift i: m-(j+1) = 6-(2+1) = 3
    Pattern:    aabaaa                  # Shift pattern (k-j) = (3-2) = 1

                aaabaadaabaaa           # k = 6, j = last(d) = -1
                      4                 # Shift i: m-(j+1) = 6-(-1+1) = 6
                 aabaaa                 # Shift pattern m = 6 characters

                aaabaadaabaaa
                       098765
                       aabaaa           # Pattern matched

    The Boyer-Moore method performs 10 comparisons before finding a match for
    the pattern.
    """
    return True


def draw_kmp():
    """Solution to exercise R-13.5.

    Repeat Exercise R-13.3 for the Knuth-Morris-Pratt algorithm, not count-
    ing the comparisons made to compute the failure function.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------

        k   |  0  1  2  3  4  5
    --------|-------------------
      P[k]  |  a  a  b  a  a  a
    --------|-------------------
      f(k)  |  0  1  0  1  2  2


    Text:       aaabaadaabaaa           # j=2, k=2, f(k-1) = f(1) = 1
                123
    Pattern:    aabaaa                  # Start comparison at j=2, k=f(1)=1

                aaabaadaabaaa           # j=6, k=5, f(k-1) = f(4) = 2
                  45678
                 aabaaa                 # Start comparison at j=6, k=f(4)=2

                aaabaadaabaaa           # j=6, k=2, f(k-1) = f(1) = 1
                      9
                    aabaaa              # Start comparison at j=6, k=f(1)=1

                aaabaadaabaaa           # j=6, k=1, f(k-1) = f(0) = 0
                      0
                     aabaaa             # Start comparison at j=6, k=f(0)=0

                aaabaadaabaaa           # j=6, k=0, j += 1
                      1
                      aabaaa            # Start comparison at j=7, k=0

                aaabaadaabaaa           # j=7, k == m-1 == 6-1 == 5
                       234567
                       aabaaa           # Pattern matched

    The Knuth-Morris-Pratt method performs 17 comparisons before finding a
    match for the pattern.
    """
    return True


def compute_map(P):
    """Solution to exercise R-13.6.

    Compute a map representing the last function used in the Boyer-Moore
    pattern-matching algorithm for characters in the pattern string:
    "the quick brown fox jumped over a lazy cat".
    """
    m = len(P)
    last = {}
    for k in range(m):
        last[P[k]] = k
    return last


def compute_kmp_table(P):
    """Solution to exercise R-13.7.

    Compute a table representing the Knuth-Morris-Pratt failure function for
    the pattern string "cgtacgttcgtac".

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------

        k   |  0  1  2  3  4  5  6  7  8  9  10 11 12
    --------|-----------------------------------------
      P[k]  |  c  g  t  a  c  g  t  t  c  g  t  a  c
    --------|-----------------------------------------
      f(k)  |  0  0  0  0  1  2  3  1  1  2  3  4  5

    """
    return compute_kmp_fail(P)


def best_multiply(chain):
    """Solution to exercise R-13.8.

    What is the best way to multiply a chain of matrices with dimensions that
    are 10 × 5, 5 × 2, 2 × 20, 20 × 12, 12 × 4, and 4 × 60? Show your work.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    My approach to solving this problem is to choose a set of parentheses that
    will result in the largest matrix dimension being multiplied by the
    smallest matrix dimension.  My intuition is that this will minimize the
    number of required multiplications.  In this problem, the largest dimension
    is 60 and the smallest dimension is 2.

        (10x5 * 5x2) * (((2x20 * 20x12) * 12x4) * 4x60)

    =   (10x2) * ((2x12 * 12x4) * 4x60)     -->     10*5*2 + 2*20*12 + ...

    =   (10x2) * (2x4 * 4x60)               -->     2*12*4 + ...

    =   (10x2) * (2x60)                     -->     2*4*60 + ...

    =   10x60                               -->     10*2*60

    =   2356 multiplications

    However, my intuition may not have provided the optimal answer.  One way of
    verifying my answer is to try every possible solution.  The number of
    ways to parenthesize a chain of n matrices is given by:

    P(n) =  1                   if n==1,

            n-1
            Σ P(k) * P(n-k)     if n>=2.
            k=1

    I wrote a function called parens() to recursively calculate the number of
    possibilities for n matrices.  There are 42 possible solutions for 6
    matrices.  This is a lot of possibilities to brute force, but I don't need
    to check every possible combination.  I can use the dynamic programming
    concept of breaking a problem down into subproblems, and then finding the
    optimal solution to each subproblem.

    I know that the 4x60 matrix has the largest potential number of
    multiplications, and that for my solution to be optimal I must have chosen
    the optimal order of multiplication involving the 4x60 matrix.  There are
    5 possible matrix multiplications involving the 4x60 matrix:

    1. 10x4 * 4x60 = 10*4*60 = 2400
    2. 12x4 * 4x60 = 12*4*60 = 2880
    3. 5x4  * 4x60 = 5 *4*60 = 1200
    4. 20x4 * 4x60 = 20*4*60 = 4800
    5. 2x4  * 4x60 = 2 *4*60 = 480

    I chose option 5, clearly the optimal choice.  And once this optimal choice
    is made, the chain reduces to 3 matrices and there are only 2 remaining
    possibilities:

    1. (10x5 * 5x2) * 2x60 = 10*5*2 + 10*2*60 = 1300
    2. 10x5 * (5x2 * 2x60) = 5*2*60 + 10*5*60 = 3600

    My solution chose option 1, again the optimal choice.  Therefore, my
    solution must be optimal as I chose the optimal solution to each subproblem
    at each step.
    """
    return matrix_chain(chain)


def another_common_subsequence():
    """Solution to exercise R-13.9.

    In Figure 13.8, we illustrate that GTTTAA is a longest common subse-
    quence for the given strings X and Y . However, that answer is not unique.
    Give another common subsequence of X and Y having length six.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    We can use Figure 13.8 to reconstruct another length-6 substring by reverse
    engineering the calculation of L(10,11) = 6.  The rules are as follows:

    1. x(j) == y(k) for position L(j, k)
        a. Add x(j) to the front of the sequence
        b. Continue analysis from L(j-1, k-1)

    2. x(j) != y(k) for position L(j, k)
        a. Move to the larger of L(j, k-1) and L(j-1, k)

    Repeat steps (1) and (2) until reaching some L(j, k) == 0.

    1. Starting at L(10, 11) = 6
        a. x(10) = '', y(11) = ''
        b. Add '' to sequence
        c. Continue from L(9, 10)
    2. L(9, 10) = 5
        a. x(9) = A, y(10) = G
        b. L(9, 9) = 5, L(8, 10) = 5
        c. Continue from L(9, 9)
    3. L(9, 9) = 5
        a. x(9) = A, y(9) = A
        b. Add A to sequence ''
        c. Continue from L(8,8)
    4. L(8, 8) = 4
        a. x(8) = T, y(8) = G
        b. L(8, 7) = 4, L(7, 8) = 4
        c. Continue from L(8, 7)
    5. L(8, 7) = 4
        a. x(8) = T, y(7) = T
        b. Add T to sequence 'A'
        c. Continue from L(7, 6)
    6.  L(7, 6) = 3
        a. x(7) = A, y(6) = T
        b. L(7, 5) = 3, L(6, 5) = 2
        c. Continue from L(7, 5)
    7.  L(7, 5) = 3
        a. x(7) = A, y(5) = A
        b. Add A to sequence 'TA'
        c. Continue from L(6, 4)
    8.  L(6, 4) = 2
        a. x(6) = A, y(4) = A
        b. Add A to sequence 'ATA'
        c. Continue from L(5, 3)
    9.  L(5, 3) = 1
        a. x(5) = T, y(3) = T
        b. Add T to sequence 'AATA'
        c. Continue from L(4, 2)
    10. L(4, 2) = 1
        a. x(4) = C, y(2) = A
        b. L(4, 1) = 1, L(3, 2) = 1
        c. Continue from L(4, 1)
    11. L(4, 1) = 1
        a. x(4) = C, y(1) = G
        b. L(4, 0) = 0, L(3, 1) = 0
        c. Continue from L(4, 0)
    12. L(4, 0) = 0
        a. x(4) = C, y(0) = C
        b. Add C to sequence 'TAATA'
        c. Reached L(j, k) = 0, algorithm complete

    The final answer is 'CTAATA' from X indices [4, 5, 6, 7, 8, 9] and
    Y indices [0, 3, 4, 5, 7, 9].

        0 1 2 3 4 5 6 7 8 9                     456789
    X = G T T C C T A A T A             -->     CTAATA

    Y = C G A T A A T T G A G A         -->     CTAATA
        0 1 2 3 4 5 6 7 8 9 0 1                 034579
    """
    return True


def freq_and_huffman(P):
    r"""Solution to exercise R-13.11.

    Draw the frequency array and Huffman tree for the following string:
    "dogs do not spot hot pots or cats".

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------

    Character:  ' ' a  c  d  g  h  n  o  p  r  s  t
    Frequency:   7  1  1  2  1  1  1  7  2  1  4  5

    To crate the Huffman tree, consider each character d in string X as the
    root node of a single-node binary tree.  Proceed to merge the two binary
    trees with the smallest frequencies together into one tree.  Repeat until
    only one tree is left.

    Merging frequencies of 1:

      2         2           2
     / \       / \         / \
    n   r     g   h       a   c

    Merging frequencies of 2:

        4           4
       / \         / \
      p,2 2       d,2 2
         / \         / \
        n   r       g   h

    Merging a frequency of 2 with a frequency of 4:
            6
         /     \
        4       2
       / \     / \
      p,2 2   a   c
         / \
        n   r

    Merging frequencies of 4:

            8
         /     \
        4      s,4
       / \
      d,2 2
         / \
        g   h

    Merging a frequency of 5 with a frequency of 6:
                11
             /     \
            6       t,5
         /     \
        4       2
       / \     / \
      p,2 2   a   c
         / \
        n   r

    Merging frequencies of 7:

         14
       /   \
    ' ',7  o,7

    Merging a frequency of 8 with a frequency of 11:

                      19
             /                 \
            8                   11
         /     \              /     \
        4      s,4           6       t,5
       / \                /     \
      d,2 2              4       2
         / \            / \     / \
        g   h          p,2 2   a   c
                          / \
                         n   r

    Merging a frequency of 19 with a frequency of 14:

                    33
          /                     \
         14                     19
        /   \           /                 \
      ' ',7  o,7       8                   11
                    /     \              /     \
                   4      s,4           6       t,5
                  / \                /     \
                 d,2 2              4       2
                    / \            / \     / \
                   g   h          p,2 2   a   c
                                     / \
                                    n   r


    The final tree has a root node containing a value of 33, which is equal to
    the length of the string.  The code for each character is obtained by
    tracing a path from the root to the leaf containing the character of
    interest, and associating a left child in the path with a 0 and a right
    child with a 1.

    codes = {
        ' ': '00',
        'a': '11010',
        'c': '11011',
        'd': '1000',
        'g': '10010',
        'h': '10011',
        'n': '110010',
        'o': '01',
        'p': '11000',
        'r': '110011',
        's': '101',
        't': '111'
    }
    """
    m = len(P)
    freq_array = {}
    for k in range(m):
        freq_array[P[k]] = freq_array.get(P[k], 0) + 1
    return freq_array


def draw_standard_trie():
    r"""Solution to exercise R-13.12.

    Draw a standard trie for the following set of strings:
    { abab, baba, ccccc, bbaaaa, caa, bbaacc, cbcc, cbca }.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
             ''
     /       |               \
    a        b                c
    |     /    \        /     |     \
    b    a      b      a      b      c
    |    |      |      |      |      |
    a    b      a      a      c      c
    |    |      |           /   \    |
    b    a      a          a     c   c
              /   \                  |
             a     c                 c
             |     |
             a     c


    Proposition 13.6 states:

    - The height of T is the longest string in S
      - Height of T is 6, longest length string 'bbaaaa' is length 6

    - Every internal node of T has at most |Sigma| children
      - |Sigma| = 3 (a,b,c) and no internal node exceeds 3 children

    - T has s leaves
      - T has 8 leaves, s=8 strings in sequence

    - The number of nodes of T is at most n + 1
      - n = 36, and there are 27 nodes in T

    The drawn standard trie meets all of the criteria of Proposition 13.6.
    """
    return True


def draw_compressed_trie():
    r"""Solution to exercise R-13.13.

    Draw a compressed trie for the strings given in the previous problem.

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    Standard trie:

             ''
     /       |               \
    a        b                c
    |     /    \        /     |     \
    b    a      b      a      b      c
    |    |      |      |      |      |
    a    b      a      a      c      c
    |    |      |           /   \    |
    b    a      a          a     c   c
              /   \                  |
             a     c                 c
             |     |
             a     c

    Compressed trie:

            ''
     /       |               \
    abab     b                c
           /    \         /   |     \
          aba   baa      aa   bc    cccc
                / \           / \
               aa  cc        a   c


    Proposition 13.7 states:

    - Every internal node of T has at least two children and at most d children
      - d = 3, and every internal node has either 2 or 3 children

    - T has s leaf nodes
      - s = 8, and T has 8 leaf nodes

    - The number of nodes is O(s)
      - T has 13 nodes, which is less than half of the standard trie's 27
        nodes.  n = 36, and s = 8, so it would appear that 13 nodes is more
        nearly O(s) than O(n).

    The drawn compressed trie meets all of the criteria of Proposition 13.7.
    """
    return True


def suffix_trie():
    r"""Solution to exercise R-13.14.

    Draw the compact representation of the suffix trie for the string:
    "minimize minime".

    ---------------------------------------------------------------------------
    Solution:
    ---------------------------------------------------------------------------
    X = minimize minime$

    The $ character is added to ensure that no suffix of X is a prefix of
    another suffix.

    There are n suffixes of string X, X[j:n] for j = 0, ..., n-1:

    j =                0,               1,              2,             3,
        minimize minime$, inimize minime$, nimize minime$, imize minime$,
                   4,           5,          6,         7,        8,       9,
        mize minime$, ize minime$, ze minime$, e minime$,  minime$, minime$,
            10,    11,   12,  13,  14, 15, 16
        inime$, nime$, ime$, me$,  e$,  $, ''

    Compressed trie:
                                       ''
             /                         |                   \
           m                           i                    nim
          /  \              /          |         \          /  \
         i    e$           m          nim    ze minime$   e$   ize minime$
       /   \              / \       /       \
      nim  ze minime$    /   \  ize minime$  e$
     /   \       ize minime$  e$
    /     \---> \
    ize minime$  e$

    Compressed trie (continued, same root):

                 ''
            /     |    \           \
    ze minime$    e    ' 'minime$   $
                 / \
        ' 'minime$   $


    Suffix trie:
                                            ''
           /                /             /   \        \       \     \
        0:1               1:2           2:5   6:16    7:8     8:16  15:16
        / \        /       |     \     /   \          /  \
    1:2  14:16    4:5      2:5   6:16 14:16 5:16   8:16  15:16
    /   \        /  \     /  \
    2:5  6:16   /    \   5:16 14:16
    /   \      5:16 14:16
    5:16 14:16

    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    m  i  n  i  m  i  z  e ' ' m  i  n  i  m  e  $
    """
    X = 'minimize minime$'
    paths = [
        X[0:1] + X[1:2] + X[2:5] + X[5:16],
        X[0:1] + X[1:2] + X[2:5] + X[14:16],
        X[0:1] + X[1:2] + X[6:16],
        X[0:1] + X[14:16],
        X[1:2] + X[4:5] + X[5:16],
        X[1:2] + X[4:5] + X[14:16],
        X[1:2] + X[2:5] + X[5:16],
        X[1:2] + X[2:5] + X[14:16],
        X[1:2] + X[6:16],
        X[2:5] + X[14:16],
        X[2:5] + X[5:16],
        X[6:16],
        X[7:8] + X[8:16],
        X[7:8] + X[15:16],
        X[8:16],
        X[15:16],
    ]
    return paths
