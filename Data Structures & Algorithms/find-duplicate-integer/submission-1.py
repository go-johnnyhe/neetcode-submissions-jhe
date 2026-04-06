class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 6 integers length 6
        #  1 2 3 4 2
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow