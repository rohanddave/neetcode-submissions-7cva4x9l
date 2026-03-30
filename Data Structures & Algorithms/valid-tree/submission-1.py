from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for n1, n2 in edges: 
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        visited = set() 

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False 
                if not dfs(neighbor, node):
                    return False 
            return True 
            
        if not dfs(0, -1):
            return False 
        
        return len(visited) == n
        