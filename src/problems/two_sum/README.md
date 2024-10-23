# Problem: two_sum

## Question

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Solution:

Since hashtables generally have an O(1) runtime when there are no collisions, I can optimize this with the following steps:

For index in list:

1. Check to see if `target - list[i]` exists as a key in the hashtable. If it does, return the associated index with i.

2. Add `list[i]` as a new key in the hachtable, using `i` as the `value`

Repeat until solved.

Because indexing the hashtable is O(1) and the for loop is O(n), the final running time of this is O(n).