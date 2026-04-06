class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # bruteforce, two for loops
        # if addition equals, add to counter


        # use prefix sum to check: have we seen a sum 
        # that's k less than my current sum?
        curr_sum = 0
        prefix_sums = {0: 1}
        count = 0
        for num in nums:
            curr_sum += num
            count += prefix_sums.get(curr_sum - k, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        return count