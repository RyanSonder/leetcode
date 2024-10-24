# Problem: palindrome_number

## Question:

Given an integer x, return true if x is a palindrome, and false otherwise.


## Solution:

### Time Complexity: $O(log{_1}{_0}{n})$

A palindrome only occurs when a number is the same written both forward and backward. Thus, a negative number can never be a palindrom.

1. Check to see if the number is negative. All negative numbers will return false.

2. Iterate through the digits. As we iterate, we will append the digits in reverse order.

3. Return whether the original is the same as the reversed string.

