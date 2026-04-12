from collections import defaultdict 
import heapq 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def dijkstra(): 
            adj = defaultdict(list) 
            for u, v, w in flights: 
                adj[u].append((v, w)) 
            
            dist = [[float('inf')] * (k + 2) for _ in range(n)]

            heap = [(0, src, 0)]
            while heap: 
                cost, node, edges = heapq.heappop(heap) 

                if node == dst: 
                    return cost 
                
                if cost > dist[node][edges]: 
                    continue
                
                if edges == k + 1: 
                    continue 
                
                for nei, nei_cost in adj[node]: 
                    new_cost = cost + nei_cost 
                    new_edges = edges + 1 

                    if new_cost < dist[nei][new_edges]: 
                        dist[nei][new_edges] = new_cost
                        heapq.heappush(heap, (new_cost, nei, new_edges))
            return -1
        
        def bellman_ford(): 
            dist = [float('inf')] * n 
            dist[src] = 0

            for i in range(k + 1): 
                temp = dist.copy() 
                for u, v, w in flights: 
                    temp[v] = min(temp[v], dist[u] + w)
                dist = temp 

            return dist[dst] if dist[dst] != float('inf') else -1
        return bellman_ford()
        