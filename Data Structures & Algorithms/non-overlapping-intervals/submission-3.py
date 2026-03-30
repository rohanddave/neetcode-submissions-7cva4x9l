class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def does_overlap(a, b): 
            return not (a[1] <= b[0] or a[0] >= b[1])
        
        intervals.sort(key=lambda x: x[1])

        curr, count = 0, 0

        for i in range(1, len(intervals)): 
            if does_overlap(intervals[curr], intervals[i]): 
                count += 1
            else: 
                curr = i
        return count
        