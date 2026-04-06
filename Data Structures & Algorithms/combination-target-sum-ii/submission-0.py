class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # use backtrack
        # stopping condition, when > target, return
        #                         == target, append to res
        # for loop over to backtrack

        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(idx, curr_sum, combo):
            if curr_sum == target:
                res.append(combo[:])
                return
            if idx == n or curr_sum > target:
                return

            
            combo.append(candidates[idx])
            dfs(idx+1, curr_sum+candidates[idx], combo)
            combo.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            dfs(idx + 1, curr_sum, combo)
        dfs(0, 0, [])
        return res