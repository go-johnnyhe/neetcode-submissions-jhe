class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # if adding to the end, we get target, return 1, otherwise 0
        # try for both that and minus that num

       
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum - nums[i]] += count
                dp[i+1][cur_sum + nums[i]] += count
        return dp[len(nums)][target]