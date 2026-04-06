class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []

        def backtrack(index, sumVal):
            if sumVal > target:
                return
            if sumVal == target:
                res.append(combo.copy())
            
            for i in range(index, len(nums)):
                combo.append(nums[i])
                backtrack(i, sumVal + nums[i])
                combo.pop()
        backtrack(0,0)
        return res