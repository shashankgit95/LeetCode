# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(nums: list[int]) -> int:
        uniq_num = 1
        if len(nums) == 1:
            return uniq_num
        for i in range(1,len(nums)):
            if(nums[i] != nums[i-1]):
                nums[uniq_num] = nums[i]
                uniq_num = uniq_num + 1

        return uniq_num
    
    nums_for_test = [0,0,1,1,1,2,2,3,3,4]
    a = removeDuplicates(nums_for_test)
    print(a,nums_for_test)






                