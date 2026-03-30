class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [i for i in range(n)]

        def union(a, b):
            rootA = find(a)
            rootB = find(b) 

            if rootA != rootB:
                graph[rootB] = rootA
        
        def find(a):
            if graph[a] != a:
                graph[a] = find(graph[a])
            return graph[a]
        
        for edge in edges:
            union(edge[0], edge[1])
        
        res = set() 
        for i in range(n):
            res.add(find(i))
        return len(res)
        