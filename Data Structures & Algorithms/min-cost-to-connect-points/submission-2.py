import heapq

class UnionFind:
    def __init__(self, n): 
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
    
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y): 
        px, py = self.find(x), self.find(y) 
        if px == py:
            return False 
        
        # assume x is bigger 
        if self.size[px] < self.size[py]:
            px, py = py, px
        
        self.parent[py] = px
        self.size[px] += self.size[py]

        self.components -= 1
        return True 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def compute_cost(p1, p2): 
            x1, y1 = p1 
            x2, y2 = p2 

            return abs(x1 - x2) + abs(y1 - y2)
    
        n = len(points) 
        edges = [] 
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((compute_cost(points[i], points[j]), i, j))
        
        edges.sort() 
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0

        for cost,u,v in edges: 
            if uf.union(u, v): 
                mst_cost += cost
                edges_used += 1
                if edges_used == n - 1: 
                    break
        
        return mst_cost
        





