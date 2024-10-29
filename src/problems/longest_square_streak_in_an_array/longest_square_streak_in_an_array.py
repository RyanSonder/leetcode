# https://leetcode.com/problems/longest-square-streak-in-an-array/

from typing import List


class longest_square_streak_in_an_array:

    def solution(nums: List[int]) -> int:
               
        def recur(nums: List[int], num: int):
            if num**2 in  nums:
                return recur(nums, num**2) + 1
            else:
                return 1
               
        nums.sort()
        
        longest = -1
        for num in nums:
            streak = recur(nums, num)
            if streak > longest:
                longest = streak
            
        return longest if longest != 1 else -1
        