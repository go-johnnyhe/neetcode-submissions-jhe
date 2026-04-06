class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCount = nums[0]
        count = 0
        for i in range(len(nums)):
            if count < 0:
                count = 0
            count += nums[i]
            maxCount = max(count, maxCount)
        return maxCount