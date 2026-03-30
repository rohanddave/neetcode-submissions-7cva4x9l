class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        def doesOverlap(interval1, interval2):
            return not (interval1[0] >= interval2[1] or interval1[1] <= interval2[0])
        
        l, count = 0, 0 
        for r in range(1, len(intervals)): 
            if doesOverlap(intervals[l], intervals[r]):
                count += 1
            else:
                l = r
        return count

        