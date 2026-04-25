class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        coins.sort()
        def dfs(i, target): 
            if target == 0:
                return 1
            if target < 0 or i == len(coins):
                return 0
            if (i, target) in memo: 
                return memo[(i, target)]
            
            pick = dfs(i, target - coins[i])
            skip = dfs(i + 1, target)
            memo[(i, target)] =  pick + skip
            return memo[(i, target)]
        return dfs(0, amount)