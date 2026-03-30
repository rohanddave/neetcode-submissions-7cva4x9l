from collections import defaultdict 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list) 

        for src, dst in tickets: 
            adj[src].append(dst) 

        for src in adj: 
            adj[src].sort(reverse=True) 
        
        res = [] 
        def dfs(airport): 
            # some base case 

            while adj[airport]: 
                popped = adj[airport].pop()
                dfs(popped)
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]

        