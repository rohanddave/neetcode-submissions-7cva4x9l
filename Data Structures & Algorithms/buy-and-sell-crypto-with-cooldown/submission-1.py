from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Decision: buy, sell or hold
        Invariant: sell date > buy date and buy again date > sell date + 1
        State: current day & HOLD / SOLD / REST
        Result: maximum profit

        max profit is achieved when you buy on a cheap day and sell on an expensive day 

        '''
        HOLD, SOLD, REST = 0, 1, 2
        @lru_cache
        def dfs(i, state): 
            # base case
            if i >= len(prices):
                return 0
            
            '''
            if i'm holding a stock meaning i can sell or keep holding; i cannot buy more than one 
            if i've sold on this day meaning i cannot buy tomorrow i.e. can only skip the next day (cool down)
            if i'm resting today meaning i can don't own a stock so i can either buy or skip today
            '''
            if state == HOLD:
                sell = prices[i] + dfs(i + 1, SOLD)
                keep = dfs(i + 1, HOLD)
                return max(sell, keep)
            elif state == SOLD: 
                return dfs(i + 1, REST)
            elif state == REST: 
                buy = -prices[i] + dfs(i + 1, HOLD) # handles cooldown
                skip = dfs(i + 1, REST)
                return max(buy, skip)          
        
        return dfs(0, REST)

        