# https://leetcode.com/problems/contains-duplicate/

class contains_duplicate:

    def solution(nums):
        nums_dict = {}
        # Iterate through the tree
        for i in range(len(nums)):

            # If we detect a match already in the dictionary
            if nums[i] in nums_dict:
                # Match has been found
                return True
            else:
                # Add a dict entry {value: index}
                nums_dict[nums[i]] = i

        # No match has been found
        return False