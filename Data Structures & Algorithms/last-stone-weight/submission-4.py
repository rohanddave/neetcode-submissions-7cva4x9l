import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        lst = [-x for x in stones]
        heapq.heapify(lst)
        while len(lst) >= 2:
            first, second = -1 * heapq.heappop(lst), -1 * heapq.heappop(lst)
            if first != second:
                heapq.heappush(lst, -1 * abs(first - second))
        return 0 if not lst else -1 * heapq.heappop(lst)