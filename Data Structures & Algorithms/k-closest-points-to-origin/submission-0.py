import math
import heapq

class Solution:
    def getDistance(self, point: List[int]):
        x, y = point[0], point[1]
        return math.sqrt(x**2 + y**2)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (self.getDistance(point), point))
        values = heapq.nsmallest(k, heap)
        res = []
        for value in values:
            res.append(value[1])
        return res

        