# Problem: roman_to_integer

## Question:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


## Solution:

### Time Complexity:

$O(n)$


### Runtime:

7 ms : Beats 95.74%%


### Memory:

16.77 MB : Beats 21.25%


### Thought Process:

1. We initialize the values of the numerals with a dictionary, since dictionaries can be used in constant time.

2. We initialize ```python sum = 0``` to keep a running total as we iterate through the string.

3. We initialize ```python flag = False``` to keep track of whether we skip a character due to the doubles in the dictionary.

4. Now we use a for loop to iterate through the string.

> If the flag is true, disable the flag and skip

> If a double char sequence is detected in the dict, use that value and enable the flag

> If no double char sequence is detected, just use the single character

5. Return the final sum
