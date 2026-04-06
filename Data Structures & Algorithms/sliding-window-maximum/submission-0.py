class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # bruteforce:
        res = []
        for i in range(0, len(nums) - k + 1):
            maxVal = float('-inf')
            for j in range(i, i + k):
                # print(nums[j])
                maxVal = max(maxVal, nums[j])
            res.append(maxVal)
            maxVal = float('-inf')
        return res