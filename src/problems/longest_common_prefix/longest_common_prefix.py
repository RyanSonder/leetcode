# https://leetcode.com/problems/longest-common-prefix/

class longest_common_prefix:

    def solution(strs):
        
        if len(strs) is 1: # Base case
            return strs[0]
        
        # Check each string in the array
        gcs = strs[0]
        for str in strs[1:]:
            
            for i in range(min(len(str), len(gcs))):
                if str[:i] != gcs[:i]:
                    continue
        
            i = 1
            while i <= min(len(str), len(gcs)):
                if str[:i] != gcs[:i]:
                    break
                i += 1
            gcs = gcs[:i - 1]

        return gcs