# Problem: product_of_array_except_self

## Question:

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


## Solution:

### Time Complexity:

$O(n)$


### Runtime:

26 ms : Beats 51.48%


### Memory:

22.46 MB : Beats 92.96%


### Thought Process:

Since answer[i] is not the product of nums[i], that means that it must be the product of all the numbers to the right and to the left. We can summarize this by calling the left numbers ```prefix``` and the right numbers ```suffix```. answer[i] is always going to be ```prefix*suffix```.

We can use loops to keep a running calculation of the ```prefix``` and ```suffix``` variables. The first loop appends each prefix to the ```prods``` array. The second loop performs the aformentioned ```prefix*suffix``` calculation.