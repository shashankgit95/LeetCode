class Solution:
    def getConcatenation(nums: list[int]) -> list[int]:
        return nums+nums
        
    nums = [1,2,1]
    ans = getConcatenation(nums)
    print(ans)