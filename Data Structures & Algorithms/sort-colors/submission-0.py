class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pass:
        # count zeros, ones, twos ==> put them in
        zeros, ones, twos = 0, 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2
                twos -= 1
