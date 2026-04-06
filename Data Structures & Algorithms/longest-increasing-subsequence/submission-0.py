from functools import lru_cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        @lru_cache
        def dfs(idx, prev_idx):
            if idx == len(nums):
                return 0
            
            best = dfs(idx+1, prev_idx)
            if prev_idx == -1 or nums[prev_idx] < nums[idx]:
                res = 1 + dfs(idx+1, idx)
                best = max(best, res)
            return best
        return dfs(0, -1)