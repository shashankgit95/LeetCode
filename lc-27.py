class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        nums_length = len(nums)
        if(nums_length == 0):
            return nums_length
        curr_val = 0
        for i in range(0,nums_length):
            if nums[i] != val:
                nums[curr_val] = nums[i]
                curr_val += 1

        return curr_val
    

    nums = [3,2,2,3]
    val = 3
    a = removeElement(nums,val)
    print(a,nums)