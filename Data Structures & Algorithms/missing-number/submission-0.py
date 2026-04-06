class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)  
      xor = n
      for i in range(len(nums)):
        xor = xor ^ i ^ nums[i]
      return xor