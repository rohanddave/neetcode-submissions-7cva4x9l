class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1): 
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])
        # n = len(cost)
        # memo = {} 

        # def dfs(i): 
        #     if i >= n:
        #         return 0
        #     if i in memo: 
        #         return memo[i]
        #     memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return memo[i]
        # return min(dfs(0), dfs(1))
        