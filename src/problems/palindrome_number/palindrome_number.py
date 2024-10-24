# https://leetcode.com/problems/palindrome-number/

class palindrome_number:

    def solution(x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reversed = 0

        while (x > 0):
            reversed = (reversed * 10) + (x % 10)
            x = int(x / 10)

        return original == reversed