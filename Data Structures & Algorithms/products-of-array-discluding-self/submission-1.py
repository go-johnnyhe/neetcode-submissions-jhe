class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6]
        # [48,24,12,8]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]
        return res