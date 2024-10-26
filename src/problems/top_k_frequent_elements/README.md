# Problem: top_k_elements_in_list

## Question:

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.


## Solution:

### Time Complexity:

$O(nlog(n))$


### Runtime:

3 ms : Beats 99.03%


### Memory:

20.29 MB : Beats 94.41%


### Thought Process:

The problem is deceptively simple.

1. We make a dictionary to easily and quickly count the number of occurrences of each value in the nums array.

2. The for loop handles counting.

3. Return a k-sized slice after using sorted to turn the dict into an array of keys sorted by their values.
