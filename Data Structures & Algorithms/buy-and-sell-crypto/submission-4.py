class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = prices[0]
        result = 0
        for sp in prices[1:]:
            result = max(result, sp - cp)
            if sp < cp:
                cp = sp
        return result

        