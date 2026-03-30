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
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        self.components -= 1

        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges) + 1)
        edge = None
        for u,v in edges: 
            if not uf.union(u, v):
                edge = [u,v]
        return edge


        