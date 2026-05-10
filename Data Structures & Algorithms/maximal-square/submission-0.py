class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r, c): 
            if r >= m or c >= n:
                return 0 
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = 0 
            if matrix[r][c] == "1": 
                right = dfs(r, c + 1)
                down = dfs(r + 1, c) 
                diag = dfs(r + 1, c + 1)
                res = 1 + min(right, down, diag)
            
            memo[(r, c)] = res
            return memo[(r, c)]
        max_side = 0
        for i in range(m):
            for j in range(n): 
                max_side = max(max_side, dfs(i, j))
        return max_side ** 2
        