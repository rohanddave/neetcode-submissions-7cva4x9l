from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list 
        # maintain a global visited 
        # iterate over 1 - n
        # for each node perform dfs / bfs 
        # once dfs or bfs is over increment count 
        # TODO: think about how to handle undirected graph 

        adj = defaultdict(list)

        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set() 
        count = 0 

        def dfs(node): 
            if node in visited: 
                return 
            
            visited.add(node)

            for neighbor in adj[node]: 
                if neighbor not in visited: 
                    dfs(neighbor)

        for i in range(n): 
            if i not in visited: 
                dfs(i)
                count += 1
        return count


        