class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # if adding to the end, we get target, return 1, otherwise 0
        # try for both that and minus that num

        from functools import lru_cache
        @lru_cache
        def dfs(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0
            return (dfs(i+1, curr_sum + nums[i]) + dfs(i+1, curr_sum - nums[i]))
        return dfs(0, 0)