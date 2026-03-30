class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # total perimeter = sum of array; if sum % 4 == 0 then true 
        # target = perimeter / 4 = size of one side 
        perimeter = sum(matchsticks)
        target = perimeter // 4
        sides = [0] * 4
        if perimeter % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        def dfs(start): 
            if start == len(matchsticks):
                return True 
            
            for i in range(len(sides)):
                if sides[i] + matchsticks[start] <= target:
                    sides[i] += matchsticks[start]
                    if dfs(start + 1):
                        return True
                    sides[i] -= matchsticks[start]
            return False
        return dfs(0)


        