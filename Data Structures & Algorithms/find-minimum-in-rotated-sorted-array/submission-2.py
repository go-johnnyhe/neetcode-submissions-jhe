class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = float('inf')
        while l <= r:
            # check two cases, could be in the left or right
            # if mid <= right, it has to be on the left (including mid)
            # else: has to be on the right
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                minimum = min(minimum, nums[mid])
                r = mid - 1
            else:
                l = mid + 1
        return minimum