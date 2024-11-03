# Problem: rotate_string

## Question:

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


## Solution:

### Time Complexity:

$O(n<sup>2</sup>)$


### Runtime:

0 ms : Beats 100%


### Memory:

16.70 MB : Beats 9.22%


### Thought Process:

First, we check characters in goal until we find one that matches the first character in s. If we find a match, match every letter in both strings based on the offset. If there is a discrepency, exit the inner loop and search for a new match for s[0]. Repeat until a solution is found or there are no more matches.
