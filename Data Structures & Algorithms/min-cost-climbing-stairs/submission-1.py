class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            one = cost[i] + dfs(i + 1)
            two = cost[i] + dfs(i + 2)
            
            memo[i] = min(one, two)
            return memo[i]
        
        return min(dfs(0), dfs(1))
        