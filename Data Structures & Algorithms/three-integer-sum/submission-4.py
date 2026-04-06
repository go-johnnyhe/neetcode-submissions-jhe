class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # -4,-1,-1,0,1,2
        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue
            start, end = i + 1, len(nums) - 1
            while start < end:
                threeSum = nums[start] + nums[end] + val
                if threeSum < 0:
                    start += 1
                elif threeSum > 0:
                    end -= 1
                else:
                    res.append([val, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return res
