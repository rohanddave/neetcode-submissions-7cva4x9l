class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list) 
        for u, v, w in flights: 
            adj[u].append((v, w))
        
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            temp = dist.copy()
            for u in adj: 
                for v, w in adj[u]:
                    temp[v] = min(temp[v], dist[u] + w)
            dist = temp
        return -1 if dist[dst] == float('inf') else dist[dst]

