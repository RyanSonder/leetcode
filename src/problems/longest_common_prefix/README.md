# Problem: longest_common_prefix

## Question:

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


## Solution:

### Time Complexity:

$O(m*n)$

n is len of the array
m is len of the strings


### Runtime:

11 ms : Beats 90.14%


### Memory:

16.84 MB : Beats 9.64%


### Thought Process:

1. There exists a base case testable in O(1) time. If the length of the array is 1, we know that the only string will be the longest prefix.

2. Store the first string in a greatest commong substring variable ```gcs```.

3. Iterate through the array.

4. For each string in the array, compare a slice from that string to a slice from gcs until they no longer match.

5. Set gcs to the last slice where it matched the str slice.

6. After done with the loops, return gcs.