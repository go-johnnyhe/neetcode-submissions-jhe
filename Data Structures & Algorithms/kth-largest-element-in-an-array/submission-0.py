class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. sort and go to -kth index
        nums.sort()
        return nums[-k]