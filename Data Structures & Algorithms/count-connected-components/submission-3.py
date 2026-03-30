class UnionFind: 
    def __init__(self, n):
        self.size = [1] * n 
        self.parent = [i for i in range (n)]
        self.components = n 
    
    def find(self, x):
        if self.parent[x] != x:
            # x = find(self.parent[x])
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): 
        px, py = self.find(x), self.find(y)
        # there is a cycle
        if px == py:
            return False
        
        if self.size[px] < self.size[py]:
            px, py = py, px
        # py is smaller 
        self.parent[py] = px 
        self.size[px] += self.size[py]

        self.components -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges: 
            uf.union(u ,v)
        return uf.components
        