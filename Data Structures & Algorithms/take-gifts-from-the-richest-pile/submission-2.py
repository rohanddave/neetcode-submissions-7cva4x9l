import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for i, gift in enumerate(gifts): 
            heapq.heappush(heap, -gift)
        
        for _ in range(k): 
            g = heapq.heappop(heap)
            heapq.heappush(heap,-1 * math.floor((- 1 * g) ** (1/2)))

        return -sum(heap)

        