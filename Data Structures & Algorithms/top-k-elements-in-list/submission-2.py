import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        for num in nums: 
            if num in freq.keys():
                freq[num] += 1
            else:
                freq[num] = 1
        
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
        
        n_largest = heapq.nlargest(k, heap)
        res = []

        for item in n_largest:
            res.append(item[1])
            
        return res

