class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        def doesOverlap(interval1, interval2):
            return not (interval1[0] > interval2[1] or interval1[1] < interval2[0])
        
        i = 0 
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < len(intervals) and doesOverlap(intervals[i], newInterval):
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
        