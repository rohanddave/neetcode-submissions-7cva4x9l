class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1): 
            for coin in coins: 
                rem = i - coin
                if rem >= 0:
                    dp[i] = min(dp[i], 1 + dp[rem])
        return -1 if dp[amount] == float('inf') else dp[amount]
        # memo = {} 

        # def dfs(target): 
        #     if target == 0:
        #         return 0
        #     if target < 0:
        #         return float('inf')
        #     if target in memo:
        #         return memo[target]
            
        #     ways = float('inf')
        #     for coin in coins: 
        #         ways = min(ways, dfs(target - coin))

        #     memo[target] = ways + 1
        #     return memo[target]
        # res = dfs(amount)
        # return -1 if res  == float('inf') else res