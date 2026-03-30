class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n 
        prices[src] = 0 

        for i in range(k + 1): 
            temp = prices.copy() # this stores the cheapest cost using i edges 
            for u, v, price in flights: 
                if prices[u] != float('inf'):
                    temp[v] = min(temp[v], prices[u] + price)
            prices = temp 
        return prices[dst] if prices[dst] != float('inf') else -1
