class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total, res = 0, 0 

        for i in range(len(gas)): 
            total += gas[i] - cost[i] 
            if total < 0: 
                total = 0
                res = i + 1
        return res

        # def dfs(i, tank, count): 
        #     if count == len(gas):
        #         return True
        #     # if we cannot get to the next station return -1 
        #     if tank + gas[i] < cost[i]:
        #         return False
            
        #     return dfs((i + 1) % len(gas), tank + gas[i] - cost[i], count + 1)
        
        # for i in range(len(gas)):
        #     if dfs(i, 0, 0):
        #         return i 
        # return -1
            
        