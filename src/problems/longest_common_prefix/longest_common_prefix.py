# https://leetcode.com/problems/longest-common-prefix/

class longest_common_prefix:

    def solution(strs):
        
        if len(strs) is 1:
            return strs[0]
        
        gcs = strs[0]
        
        for str in strs[1:]:
        
            i = 1
            while i <= len(gcs):
                if str[:i] != gcs[:i]:
                    break
                i += 1

            gcs = gcs[:i-1]

        return gcs