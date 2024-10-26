# https://leetcode.com/problems/top-k-frequent-elements/


class top_k_frequent_elements():

    def solution(nums, k):
        r = {}

        for n in nums:
            if n not in r:
                r[n] = 1
            else:
                r[n] = r[n] + 1

        return [k for k, v in sorted(r.items(), key=lambda item: item[1])][-k:]
