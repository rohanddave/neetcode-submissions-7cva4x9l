from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def hasCycle(node, parent): 
            if node in visited:
                return True
            
            visited.add(node)
            
            for child in adj[node]:
                if child == parent:
                    continue 
                if hasCycle(child, node):
                    return True
            return False
        
        if hasCycle(0, -1):
            return False
        
        return len(visited) == n
        

        