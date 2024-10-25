# Problem: contains_duplicate

## Question:

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


## Solution:

### Time Complexity:

$O(n)$


### Runtime:

13 ms : Beats 94.80%


### Memory:

37.07 MB : Beats 6.22%


### Thought Process:

Worst case scenario, every element in the array is different. The array will need to be checked at every index in the array in O(n) time.

Best case scenario, the first two elements match, and the program runs in O(1) time.

1. We initiate an empty dictionary. This will be used to store values already accessed in the array, since a dictionary can be accessed in O(1) time.

2. Iterate through the array to check each number.

* If the value at the current pointer is found in the dict, a match has been found: ```return True```

* If the value at the current pointer is not found in the dict, add it.

3. If we iterate through each element in the array and find no matches: ```return False```