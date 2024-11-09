# Problem: check_balanced_string

## Question:

You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.


## Solution:

### Time Complexity:

$O(n)$


### Runtime:

0 ms : Beats 100%


### Memory:

16.75 MB : Beats 9.14%


### Thought Process:

This solution uses a temporary variable to keep a running total of the numbers. As we iterate through each digit, we add that digit and then multiply the temporary variable by -1. This means that we only do not need to keep track of when to add and when to subtract. No matter what, if the number is balanced, the final answer should be 0.
