class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dfs(i): 
            if i >= len(days):
                return 0 
            if i in memo:
                return memo[i]
            
            choices = [1, 7, 30]
            res = float('inf')
            for j, choice in enumerate(choices): 
                coverage_end = days[i] + choice
                l, r = i + 1, len(days) 
                while l < r:
                    m = (l + r) // 2
                    if days[m] >= coverage_end: 
                        r = m
                    else:
                        l = m + 1
                res = min(res, costs[j] + dfs(l))
            memo[i] = res 
            return memo[i]
        return dfs(0)
                
        