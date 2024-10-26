# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict


class top_k_frequent_elements():

    def solution(nums, k):
        ranking = defaultdict(int)

        for n in nums:
            ranking[n] += 1

        return [k for k, v in sorted(ranking.items(), key=lambda item: item[1])][-k:]
