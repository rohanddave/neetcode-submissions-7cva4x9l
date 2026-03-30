from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list) 

        for src, dst in tickets: 
            adj[src].append(dst) 
        
        for src in adj.keys(): 
            adj[src].sort()
        start = "JFK"
        res = [start] 

        def dfs(node): 
            if len(res) == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            temp = adj[node].copy()
            for i, nei in enumerate(temp): 
                popped = adj[node].pop(i)
                res.append(popped)
                if dfs(nei):
                    return True 
                adj[node].insert(i, nei)
                res.pop()
            
        
        dfs(start)
        return res



        