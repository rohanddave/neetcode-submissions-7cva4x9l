class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        res = []
        memo = {} 

        def dfs(i): 
            if i == n: 
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            
            count = dfs(i + 1)
            if (i + 1) < n and 10 <= int(s[i: i + 2]) <= 26:
                count += dfs(i + 2)
            memo[i] = count
            return memo[i]
        return dfs(0)
        