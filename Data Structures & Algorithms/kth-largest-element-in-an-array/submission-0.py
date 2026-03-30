import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            heapq.heappush(res, num)
        return heapq.nlargest(k, res)[k -1]
        