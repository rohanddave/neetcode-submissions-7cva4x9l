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
            return [x + 1, y + 1]
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
        self.components -= 1

        return None
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        edge = None
        for u,v in edges: 
            res = uf.union(u - 1, v - 1)
            if res: 
                edge = res
        return edge


        