import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries_heap = []
        for i, query in enumerate(queries): 
            heapq.heappush(queries_heap, (query, i))

        heap = [] 
        intervals.sort(key=lambda x: x[0])
        i, n = 0, len(intervals)
        res = [-1] * len(queries)

        while queries_heap: 
            query, index = heapq.heappop(queries_heap) 

            while i < n and intervals[i][0] <= query: 
                interval_size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(heap, (interval_size, intervals[i][1]))
                i += 1
            
            while heap and heap[0][1] < query: 
                heapq.heappop(heap)
            
            if heap: 
                res[index] = heap[0][0]
        return res




        