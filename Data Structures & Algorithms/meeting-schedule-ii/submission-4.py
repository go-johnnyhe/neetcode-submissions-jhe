"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        maxCount, count = 0, 0
        startIndex, endIndex = 0, 0
        # 0, 5, 15
        # 10, 20, 40
        while startIndex < len(intervals):
            if start[startIndex] < end[endIndex]:
                count += 1
                startIndex += 1
            else:
                count -= 1
                endIndex += 1
            maxCount = max(count, maxCount)
        return maxCount
