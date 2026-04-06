class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # one pointer stays put, other two adds to it
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,0,1,1,2]
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[0] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result