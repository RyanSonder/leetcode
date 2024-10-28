# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class product_of_array_except_self:

    def solution(nums: List[int]) -> List[int]:
        len_nums = len(nums)
        
        # Create array that will hold product values
        prods = []
        
        # Iterate over nums to mul prefix
        prefix = 1        
        for i, num in enumerate(nums):
            prods.append(prefix)
            prefix *= num
            
        # Do the same for suffix
        suffix = 1
        for i, num in enumerate(reversed(nums)):
            prods[len_nums - i - 1] *= suffix
            suffix *= num
        
        return prods    
