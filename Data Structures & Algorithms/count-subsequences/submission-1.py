class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j): 
            if j == len(t): 
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # if characters match
            
            exclude = dfs(i + 1, j)
            res = exclude
            if s[i] == t[j]: 
                include = dfs(i + 1, j + 1)
                res += include
            memo[(i, j)] = res
            return memo[(i ,j)]
        return dfs(0, 0)
        