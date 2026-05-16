class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        ans = nums
        for i in range(num_len):
            num = nums[i]
            ans.append(num)
        return ans