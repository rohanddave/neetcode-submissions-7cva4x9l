class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        fewest number of coins needed to make amount 
        return -1 if not possible 

        state: remaining amount 
        invariant: remaining amount >= 0 and i < len(coins)
        dfs function retuns the minimum number coins required to make amount from 0-ith coin
        '''
        memo = {}
        def dfs(target):
            if target == 0:
                return 0
            if target in memo:
                return memo[target]
            
            res = float('inf')
            for coin in coins: 
                if coin > target:
                    continue 
                res = min(res, 1 + dfs(target - coin))
            memo[target] = res
            return memo[target]
        res = dfs(amount)
        return -1 if res == float('inf') else res
                
        