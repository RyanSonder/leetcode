# https://leetcode.com/problems/valid-anagram/

class valid_anagram:

    def solution(s: str, t: str) -> bool:
        
        # Base case
        if len(s) != len(t):
            return False

        l = len(s) # Store len for performance efficiency
        
        # Store s into a dict as {char: number}
        d = {}
        for i in range(l):
            if s[i] not in d:
                # Add char to dict
                d[s[i]] = 1
            else:
                # Increment number of the char
                d[s[i]] += 1

        # Decrement dict entries while iterating through t
        for i in range(l):
            if t[i] not in d or d[t[i]] == 0:
                # Char not in dict or too many char compared to first string
                return False
            else:
                # Decrement the entry to indicate traversal
                d[t[i]] -= 1

        # Check to make sure each dict entry is 0
        for v in d.values():
            if v != 0:
                return False
            
        return True