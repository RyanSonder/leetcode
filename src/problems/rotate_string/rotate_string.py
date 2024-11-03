# https://leetcode.com/problems/rotate-string/

class rotate_string:

    def solution(s: str, goal: str) -> bool:
        length = len(s)
        
        if length != len(goal):
            return False
        
        for i in range(length):
            if s[0] == goal[i]:
                flag = True
                for j in range(length):
                    if s[j] != goal[(i + j) % (length)]:
                        flag = False
                        break 
                if flag:
                    return True
            
        return False