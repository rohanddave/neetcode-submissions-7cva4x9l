import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def does_overlap(interval, query): 
            return interval[0] <= query <= interval[1]

        n, m = len(intervals), len(queries)
        res = [-1] * m
        queries_heap = [] 
        for i, query in enumerate(queries): 
            heapq.heappush(queries_heap, (query, i))
        
        heap = [] 
        i = 0 

        intervals.sort(key=lambda x: x[0])
        while queries_heap: 
            query, idx = heapq.heappop(queries_heap)

            while i < n and intervals[i][0] <= query:
                interval_size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (interval_size, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < query: 
                heapq.heappop(heap)
            
            if heap: 
                res[idx] = heap[0][0]
        return res