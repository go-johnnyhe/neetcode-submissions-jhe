class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # permutations, try backtracking
        #    []
        #  1               []
        # 12 1            2  []
        # 123 12 13 1    23 2  3 []
        res = []
        subset = []
        def backtracking(index):
            if index == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            backtracking(index + 1)
            subset.pop()
            backtracking(index + 1)

        backtracking(0)
        return res