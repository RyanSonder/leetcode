# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

class group_anagrams:

    def solution(strs):

        d=defaultdict(list)

        for i in strs:
            d[''.join(sorted(i))].append(i)
        return list(d.values())