"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def does_overlap(a ,b): 
            return not (a.end <= b.start or a.start >= b.end)

        intervals.sort(key=lambda x: x.start)
        curr = 0

        for i in range(1, len(intervals)):
            if does_overlap(intervals[curr], intervals[i]):
                return False
            
            curr = i
        return True

