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

        curr, max_rooms = 0, 0 
        for _, delta in events: 
            curr += delta 
            max_rooms = max(max_rooms, curr)
        return max_rooms
        