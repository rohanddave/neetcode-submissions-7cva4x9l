class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} 

        def dfs(target): 
            if target == 0:
                return 0
            if target < 0:
                return float('inf')
            if target in memo:
                return memo[target]
            
            ways = float('inf')
            for coin in coins: 
                ways = min(ways, dfs(target - coin))

            memo[target] = ways + 1
            return memo[target]
        res = dfs(amount)
        return -1 if res  == float('inf') else res