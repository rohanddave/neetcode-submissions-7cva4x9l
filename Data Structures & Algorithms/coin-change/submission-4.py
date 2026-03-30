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
            
            count = float('inf') 
            for coin in coins: 
                count = min(count, 1 + dfs(target - coin))
            memo[target] = count
            return count
        res = dfs(amount)
        return -1 if res == float('inf') else res
        

            
        