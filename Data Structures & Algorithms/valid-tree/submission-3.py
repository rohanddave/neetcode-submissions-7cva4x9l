from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set() 
        
        def hasCycle(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return True
                if hasCycle(neighbor, node):
                    return True
                
        
        if hasCycle(0, -1):
            return False

        return len(visited) == n