# https://leetcode.com/problems/two-sum/

class two_sum:

    def solution(nums, target):
        nums_dict = {}
        for i in range(len(nums)):

            # If we detect a match already in the dictionary
            if (target - nums[i]) in nums_dict:
                return [nums_dict[target - nums[i]], i]
            
            # We add a dict entry {value: index}
            nums_dict[nums[i]] = i