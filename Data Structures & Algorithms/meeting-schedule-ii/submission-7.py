"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # get the intervals into this format
        # sort them by both start and finish, in order, and list them out
        # [(0, start), (5, start), (10, end)] whenever it's a new meeting, increase
        # whenever it's end time, decrease by one, track the maximum
        res = []
        for i in range(len(intervals)):
            beg = intervals[i].start
            finish = intervals[i].end
            res.append((beg, "start"))
            res.append((finish, "end"))
        res.sort(key = lambda x : (x[0], 0 if x[1] == "end" else 1))
        maxCount = 0
        count = 0
        for i in range(len(res)):
            status = res[i][1]
            if status == "start":
                count += 1
                maxCount = max(maxCount, count)
            else:
                count -= 1
        return maxCount