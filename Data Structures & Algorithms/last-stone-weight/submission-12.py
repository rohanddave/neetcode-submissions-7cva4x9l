import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones: 
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)
            if s1 != s2:
                heapq.heappush(heap, -abs(s1 - s2))
        
        return 0 if not heap else -heapq.heappop(heap)
        