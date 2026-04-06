class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(curr_combo, remaining, start_i):
            if remaining == 0:
                res.append(curr_combo[:])
                return
            if remaining < 0:
                return
            for i in range(start_i, len(nums)):
                curr_combo.append(nums[i])
                backtrack(curr_combo, remaining - nums[i], i)
                curr_combo.pop()
        backtrack([], target, 0)
        return res