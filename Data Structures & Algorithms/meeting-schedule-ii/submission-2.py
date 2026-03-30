"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = [] 
        for interval in intervals: 
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        
        events.sort(key=lambda x: (x[0], x[1]))

        max_count, curr_count = 0 , 0
        for _, count in events: 
            curr_count += count
            max_count = max(max_count, curr_count)
        return max_count

        