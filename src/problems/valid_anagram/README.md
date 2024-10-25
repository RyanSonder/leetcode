# Problem: valid_anagram

## Question:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.


## Solution:

### Time Complexity:

$O(n)$


### Runtime:

15 ms : Beats 95.45%


### Memory:

16.76 MB : Beats 94.31%


### Thought Process:

1. There is a base case where the strings are different length. Checking this is O(1) time, so easy to do.

2. We store the characters in s into a dict such that {char: occurrences}

3. We check the dict, decrementing as we go to indicate traversal. If a char not present appears or there are too many copy letters, we know an anagram is invalid.

4. We now check the dict to make sure every value is 0. If any value is not 0, then s and t are not anagrams.

5. If everything passes these tests, it must be an anagram.
