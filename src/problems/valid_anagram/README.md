# Problem: valid_anagram

## Question:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.


## Solution:

### Time Complexity:

$O(n)$


### Runtime:

12 ms : Beats 96.44%


### Memory:

16.80 MB : Beats 94.31%


### Thought Process:


1. There exists a base case that can be tested in O(1) time. If the lengths of s and t do not match, the anagram is invalid.

2. Initialize an empty dictionary.

3. Iterate through both strings at the same time. For each letter, increment if in s, and decrement if in t.

4. Iterate through the dictionary. If the strings are anagrams, the values should all have zeroed out. If any values are not zeroed out, then return false.

5. The check passed, return true.