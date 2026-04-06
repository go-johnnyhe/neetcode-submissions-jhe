class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # lowest = max(nums), highest = sum(nums)
        #      ans is in this range
        # if after the for loop, the accumulated group <= k:
        # track the answer, keep going down
        # else: keep going up
        low, high = max(nums), sum(nums)
        res = high
        while low <= high:
            mid = low + (high - low) // 2
            sum_val = 0
            group_count = 1
            for num in nums:
                if sum_val + num > mid:
                    group_count += 1
                    sum_val = num
                else:
                    sum_val += num
            if group_count <= k:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res