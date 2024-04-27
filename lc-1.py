from typing import List


class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        hm = {}
        for idx, ele in enumerate(nums):
            if (target - ele) in hm:
                return [idx,hm[target - ele]]
            hm[ele] = idx
        return [0,1]
 
 
nums =[3,2,4]       
target = 6
s = Solution.twoSum(nums,target)
print(s)