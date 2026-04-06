class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # bruteforce:
        # 1, 12, 12-3, 12-34
        # 2, 2-3, 2-34
        # -3, -34
        # 4
        prev_min, prev_max, global_max = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curr_max = max(num, num * prev_min, num * prev_max)
            curr_min = min(num, num * prev_min, num * prev_max)
            global_max = max(global_max, curr_max)
            prev_min, prev_max = curr_min, curr_max
        return global_max

        