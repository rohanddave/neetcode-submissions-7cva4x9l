import heapq 
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times: 
            adj[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        visited = set()
        dist[k] = 0 
        heap = [(0, k)] 

        while heap: 
            cost, node = heapq.heappop(heap)

            if cost > dist[node]:
                continue 
            
            visited.add(node)

            for nei, nei_cost in adj[node]:
                new_cost = cost + nei_cost
                if new_cost < dist[nei]:
                    dist[nei] = new_cost
                    heapq.heappush(heap, (new_cost, nei))
        
        print(visited)
        print(dist)
        if len(visited) < n:
            return -1
        return max(dist[1:])






        