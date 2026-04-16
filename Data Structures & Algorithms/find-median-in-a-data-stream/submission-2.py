import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else: 
            heapq.heappush(self.max_heap, -num) 
        
        if len(self.min_heap) > len(self.max_heap): 
            popped = heapq.heappop(self.min_heap) 
            heapq.heappush(self.max_heap, -popped)
        elif len(self.max_heap) > len(self.min_heap) + 1: 
            popped = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, popped)
        print(self.max_heap, self.min_heap)
        

    def findMedian(self) -> float:
        length = len(self.max_heap) + len(self.min_heap)
        if length % 2 == 0: 
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]
        
        