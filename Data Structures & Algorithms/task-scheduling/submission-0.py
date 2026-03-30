from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        heap = []
        for _, freq in cnt.items():
            heapq.heappush(heap, -freq)
        q = deque()
        time = 0
        while heap or q: 
            # time += 1
            if heap:
                freq = heapq.heappop(heap) + 1
                if freq < 0:
                    q.append((freq, time + n))
            if q and time >= q[0][1]:
                heapq.heappush(heap, q.popleft()[0])
            time += 1
        return time



        