class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(target, count): 
            if target == 0:
                return count
            if target < 0:
                return float('inf')
            if (target, count) in memo:
                return memo[(target, count)]
            
            res = float('inf')
            for coin in coins: 
                res = min(res, dfs(target - coin, count + 1))

            memo[(target, count)] = res
            return memo[(target, count)]
        res = dfs(amount, 0)
        return -1 if res  == float('inf') else res

        