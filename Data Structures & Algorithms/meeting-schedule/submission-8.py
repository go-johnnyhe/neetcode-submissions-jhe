"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        if not intervals:
            return True
        end = intervals[0].end
        for interval in intervals[1:]:
            if end > interval.start:
                print(interval.start)
                print(end)
                return False
            end = interval.end
        return True