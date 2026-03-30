from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # the start is always JFK

        adj = defaultdict(list) 
        for src, dst in tickets: 
            adj[src].append(dst)
        for k in adj.keys():
            adj[k] = sorted(adj[k])
        start = "JFK"
        res = [start]
        def dfs(node):
            if len(res) == len(tickets) + 1: 
                return True
            if not adj[node]: 
                return False 
            
            temp = adj[node].copy()
            for i, nei in enumerate(temp): 
                v = adj[node].pop(i)
                res.append(v) 

                if dfs(v): 
                    return True
                
                adj[node].insert(i, v)
                res.pop()
        dfs(start)
        return res