# https://leetcode.com/problems/check-balanced-string/

class check_balanced_string:

    def solution(self, num: str) -> bool:

        tmp = 0
        for char in num:
            tmp = -(tmp + int(char))

        return tmp == 0