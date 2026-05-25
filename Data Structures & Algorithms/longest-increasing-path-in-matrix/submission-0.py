class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        def dfs(r, c): 
            if not (0 <= r < m and 0 <= c < n):
                return 0
            if (r, c) in memo: 
                return memo[(r, c)]
            
            best = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]: 
                    best = max(best, 1 + dfs(nr, nc))
            memo[(r, c)] = best
            return memo[(r, c)]
        res = 1
        for i in range(m): 
            for j in range(n): 
                res = max(res, dfs(i, j))
        return res
