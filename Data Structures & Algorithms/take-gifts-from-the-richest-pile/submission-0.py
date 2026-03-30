import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for i, gift in enumerate(gifts): 
            heapq.heappush(heap, (-gift, i))
        
        for _ in range(k): 
            g, idx = heapq.heappop(heap)
            new_g = math.floor((- 1 * g) ** (1/2))
            heapq.heappush(heap, (-1 * new_g, idx))
            gifts[idx] = new_g

        return sum(gifts)

        