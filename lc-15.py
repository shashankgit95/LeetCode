from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for idx,ele in enumerate(nums):
            first = idx
            if first > 0 and ele == nums[first - 1]:
                continue
            if(idx < len(nums) - 2):
                second = first + 1
                third = len(nums) - 1
                while(second < third):
                    value = nums[first] + nums[second] + nums[third]
                    if value == 0:
                        result.append([ele,nums[second],nums[third]])
                        second += 1
                        while nums[second] == nums[second - 1] and second < third:
                            second += 1
                    elif value > 0:
                        third -= 1
                    else:
                        second += 1
        return result
