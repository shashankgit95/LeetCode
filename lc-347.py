from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []
        for ele in nums:
            count[ele] += 1
        l = [[] for _ in range(len(nums)+1)]
        for key,value in count.items():
            l[value].append(key)
        idx = len(l) - 1
        while idx > 0 and k > 0:
            if len(l[idx]) > 0:
                result.append(l[idx].pop())
                k -= 1
            else:
                idx -= 1
        return result
