class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def does_overlap(a, b): 
            return not (a[1] <= b[0] or a[0] >= b[1])
        
        intervals.sort(key=lambda x: x[1])  # sort by END
        removals = 0
        curr = 0

        for i in range(1, len(intervals)):
            if does_overlap(intervals[curr], intervals[i]): 
                removals += 1
            else:
                curr = i           # overlap, remove current (has later end)

        return removals
        