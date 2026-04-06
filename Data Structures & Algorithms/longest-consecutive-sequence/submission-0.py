class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxSeq = 0

        for num in nums:
            if num - 1 not in nums:
                # has to be smallest or invalid
                curr_num = num
                curr_sequence = 1
                while curr_num + 1 in nums:
                    curr_num += 1
                    curr_sequence += 1
                maxSeq = max(maxSeq, curr_sequence)

        return maxSeq
