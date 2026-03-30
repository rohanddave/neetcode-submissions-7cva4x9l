from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list) 

        for src, dst in tickets: 
            adj[src].append(dst) 
        
        for src in adj.keys(): 
            adj[src].sort(reverse=True)
    
        start = "JFK"
        res = [] 

        def dfs(node): 
            while adj[node]: 
                nei = adj[node].pop()
                dfs(nei)
            res.append(node)
            
        dfs(start)
        return res[::-1]



        