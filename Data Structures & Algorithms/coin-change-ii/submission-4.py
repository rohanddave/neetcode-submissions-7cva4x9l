class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        return the number of distinct combinations that total to amount 

        state: target
        invariant: target < amount 
        dfs function: returns the number of combinations from ith coin to make target
        '''
        memo = {}
        def dfs(i, target):
            if target == 0: 
                return 1
            if target < 0 or i == len(coins): 
                return 0
            if (i, target) in memo:
                return memo[(i, target)]
            
            res = 0
            # take the current coin 
            if coins[i] <= target: 
                res += dfs(i, target - coins[i])
            # skip the current coin
            res += dfs(i + 1, target)
            memo[(i, target)] = res
            return memo[(i, target)]
        return dfs(0, amount)
        