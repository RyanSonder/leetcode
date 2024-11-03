# Problem: circular_sentence

## Question:

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

* For example, "Hello World", "HELLO", "hello world hello world" are all sentences.

Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

* The last character of a word is equal to the first character of the next word.

* The last character of the last word is equal to the first character of the first word.

For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true _if it is circular_. Otherwise, return false.

## Solution:

### Time Complexity:

$O(n)$


### Runtime:

0 ms : Beats 100%


### Memory:

16.58 MB : Beats 46.28%


### Thought Process:

This problem is exceedingly easy. This method splits the sentence into a list of words, and iterates through the words and checks if the last letter of the previous word matches the first letter of the next word. 

Then at the end there is a check to make sure the last letter of the last word is equal to the first letter of the first word.