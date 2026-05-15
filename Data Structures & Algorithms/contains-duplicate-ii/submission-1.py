class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # idea 1:
        # dictionary of values, index. if found of the condition, return True, else False
        # val_to_ind = {}
        # for i in range(len(nums)):
        #     if nums[i] in val_to_ind and abs(i - val_to_ind[nums[i]]) <= k:
        #         return True
        #     val_to_ind[nums[i]] = i
        # return False
        # sliding window O(k) space:
        window = set()
        for i, v in enumerate(nums):
            if v in window:
                return True
            window.add(v)
            if len(window) > k:
                window.remove(nums[i-k])
        return False
    