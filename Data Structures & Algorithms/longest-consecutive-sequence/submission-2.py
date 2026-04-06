class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums:
            if num - 1 not in nums_set:
                curr_num = num
                curr_streak = 0

                while curr_num in nums_set:
                    curr_num += 1
                    curr_streak += 1
                max_count = max(max_count, curr_streak)
        return max_count