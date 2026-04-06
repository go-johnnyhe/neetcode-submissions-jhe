class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        # [3,4,5,6,1,2]
        #  l   m l m r
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                res = min(nums[mid], res)
                r = mid - 1
            else:
                l = mid + 1
        return res