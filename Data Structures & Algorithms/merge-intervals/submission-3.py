class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def does_overlap(interval1, interval2): 
            return not (interval1[1] < interval2[0] or interval1[0] > interval2[1])
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if does_overlap(merged[-1], intervals[i]): # overlaps with last merged
                merged[-1] = [min(merged[-1][0], intervals[i][0]), max(merged[-1][1], intervals[i][1])]  # extend end
            else:
                merged.append(intervals[i])     # no overlap, new group

        return merged
        