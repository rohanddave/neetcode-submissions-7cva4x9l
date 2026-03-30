import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] 
        cnt = Counter(nums)
        for n, freq in cnt.items(): 
            heapq.heappush(heap, (freq, n))
            if len(heap) > k: 
                heapq.heappop(heap)
        return [n for _, n in heap]
        