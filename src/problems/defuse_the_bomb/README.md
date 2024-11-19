# Problem: Defuse The Bomb

https://leetcode.com/problems/defuse-the-bomb/

## Question:

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

## Solution:

### Time Complexity:

\$O()\$


### Runtime:

0 ms : Beats 100%


### Memory:

16.67 MB : Beats 62.60%


### Thought Process:

 - k == 0: just return an array of 0's
 - k < 0: rotate the list and use negative slicing
 - k > 0: use an extended list to avoid spending extra time looping back to the beginning for a second slice