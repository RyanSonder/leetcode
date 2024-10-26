# Problem: group_anagrams

## Question:

Given an array of strings strs, group the anagrams together. You can return the answer in any order.


## Solution:

### Time Complexity:

$O(n*k*log(k))$

n = len(strs)
k = len(str
)

### Runtime:

7 ms : Beats 99.72% 


### Memory:

19.61 MB : Beats 79.86%


### Thought Process:

This was a difficult one, until I saw someone else's solution using a defaultdict.

This solution uses a default dict because insertion to a key that does not exist just creates an entry. We make use of this by keeping track of each anagram using a sorted version of their string as the key, and a list of all matches as the values. Thus, this is a very efficient solution.

Note: This solution was not my own. I was struggling too much and could not find an elegant solution with a quick running time, so I looked at some high efficiency submissions.