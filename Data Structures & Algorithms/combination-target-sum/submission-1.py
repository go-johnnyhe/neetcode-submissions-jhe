class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #        0
        #       2                   5   6  9
        #   2. 5. 6. 9
        # achieve:
            # no duplicate answers
            # does not exceed target
            # when equal to target and not duplicate, add to results array
            # else, keep building the recursion tree
        results = []
        def backtrack(curr_combo, remaining, start_i):
            if remaining == 0:
                results.append(curr_combo[:])
                return
            elif remaining < 0:
                return
            
            for i in range(start_i, len(nums)):
                num = nums[i]
                curr_combo.append(num)
                backtrack(curr_combo, remaining - num, i)
                curr_combo.pop()
        backtrack([], target, 0)
        return results