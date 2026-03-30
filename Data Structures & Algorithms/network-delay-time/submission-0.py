from collections import defaultdict 
import heapq 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, dist in times: 
            u -= 1
            v -= 1
            adj[u].append((v, dist))
    
        dist = [float('inf')] * n
        dist[k - 1] = 0
        heap = [(0, (k - 1))]

        while heap: 
            d, n = heapq.heappop(heap)

            if d > dist[n]:
                continue
            
            for nei, nei_dist in adj[n]: 
                new_dist = d + nei_dist
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        res = max(dist)
        return res if res != float('inf') else -1