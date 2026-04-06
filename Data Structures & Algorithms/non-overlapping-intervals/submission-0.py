class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1-2. 1-4. 2-4.
        # steps: 
        # initialize count, sort the first elements in the intervals
        # if any starting element is less than the second element from earlier,
        # count+=1, and take the minor of the heights for the second element
        count = 0
        intervals.sort(key=lambda i:i[0])
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end:
                count += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end
                # add the earlier end time in
        return count