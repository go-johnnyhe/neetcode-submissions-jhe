class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # [-4,-1,-1,0,1,2]
        # iteratively set one as target, two pointer the rest
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if i == len(nums) - 2:
                break
            target = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                sumVal = target + nums[l] + nums[r]
                if sumVal == 0:
                    res.append([target, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sumVal < 0:
                    l += 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
        return res
                