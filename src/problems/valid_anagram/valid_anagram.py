# https://leetcode.com/problems/valid-anagram/


class valid_anagram:

    def solution(s: str, t: str) -> bool:

        if len(s) != len(t): 
            return False
        if s == t: 
            return True

        d = {} 
        for i in range(len(s)): 
            cs = s[i]
            ct = t[i]

            d[cs] = d.get(cs, 0) + 1
            d[ct] = d.get(ct, 0) - 1

        for n in d.values(): 
            if n != 0 : return False

        return True

        