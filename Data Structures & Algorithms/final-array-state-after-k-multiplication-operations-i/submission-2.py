import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [] 
        for i, n in enumerate(nums): 
            heapq.heappush(heap, (n, i))
        
        for i in range(k):
            num, idx = heapq.heappop(heap)
            new_num = num * multiplier
            nums[idx] = new_num
            heapq.heappush(heap, (new_num, idx))
        return nums
        