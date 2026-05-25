class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        if we reached the end of p and end of s return True 
        if we reached the end of p and not end of s return false
        if p[j].isalpha() and s[i] != p[j]: return false
        
        if s[i] == p[j] or p[j] == '.': return dfs(i + 1, j + 1)
        else:
            # this means we're at a * 
            # here we can either continue matching the prev matched or stop 
            if s[i] == s[i - 1]:
                continue = dfs(i + 1, j)
            stop = dfs(i, j + 1)
        '''
        memo = {} 
        def dfs(i, j): 
            if j == len(p): 
                return i == len(s) 
            if (i, j) in memo:
                return memo[(i, j)]
            
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*': 
                res = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else: 
                res = first_match and dfs(i + 1, j + 1)
            memo[(i, j)] = res
            return memo[(i, j)]
        return dfs(0, 0)