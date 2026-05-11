class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices[i] = price on the ith day 
        on a day: buy and/or sell 
        can hold at most one share at any time

        return max profit 

        on a day: 
        buy: only if not holding already (state: need something to track holding or not)
        sell: only if holding already (state: need something to track holding price)
        hold: always possible

        dfs function returns the profit on on the ith day 

        buy: prices[i] + dfs(i + 1, i)
        sell: 
        state: 
        1. i = current day index 
        2. j = last bought index 

        '''
        memo = {} 
        def dfs(i, holding): 
            # some base case 
            if i == len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]

            res = float('-inf')
            # buy
            if not holding:
                res = max(res, -prices[i] + dfs(i + 1, True))
            
            # sell 
            if holding: 
                res = max(res, prices[i] + dfs(i + 1, False))
            
            # skip
            res = max(res, dfs(i + 1, holding))

            memo[(i, holding)] = res
            return res
        return dfs(0, False)
        