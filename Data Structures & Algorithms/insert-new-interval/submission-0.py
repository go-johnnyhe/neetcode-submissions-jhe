class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        for i in range(len(intervals)):
            low, high = intervals[i]
            if new_end < low:
                res.append(newInterval)
                return res + intervals[i:]
            elif new_start > high:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], low), max(newInterval[1], high)]
        res.append(newInterval)
        return res