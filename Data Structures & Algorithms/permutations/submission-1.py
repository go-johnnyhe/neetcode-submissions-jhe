class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        perm = []
        length = len(nums)
        def backtrack():
            if len(perm) == length:
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    backtrack()
                    perm.pop()
        backtrack()
        return res