class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def doesOverlap(interval1, interval2):
            return not (interval1[0] > interval2[1] or interval1[1] < interval2[0]) 

        intervals.sort(key=lambda x: x[0])
                
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i] 
            prev = res[-1]
            if doesOverlap(curr, prev): 
                res[-1] = [min(curr[0], prev[0]), max(curr[1], prev[1])]
            else:
                res.append(curr)
        return res
        