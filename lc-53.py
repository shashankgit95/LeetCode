from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = n
            else:
                curSum += n
            maxSum = max(maxSum,curSum)
        return maxSum