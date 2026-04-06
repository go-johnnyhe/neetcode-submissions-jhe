"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort for intervals, check if the start time is ever past a previous end time
        intervals.sort(key = lambda x : x.start)
        if len(intervals) <= 1:
            return True
        prevStart, prevEnd = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i].start, intervals[i].end
            if prevEnd <= currStart:
                prevStart, prevEnd = currStart, currEnd
            else:
                return False
        return True