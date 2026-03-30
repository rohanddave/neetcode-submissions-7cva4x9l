"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def doesOverlap(interval1, interval2):
            return not (interval1.start >= interval2.end or interval1.end <= interval2.start)
        l = 0 
        for r in range(1, len(intervals)):
            if doesOverlap(intervals[l], intervals[r]):
                return False
            l += 1
        return True 
