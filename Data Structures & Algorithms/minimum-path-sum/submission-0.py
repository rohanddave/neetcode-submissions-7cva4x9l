class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}
        def dfs(i, j): 
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            
            right = down = float('inf')
            if (j + 1) < n:
                right = grid[i][j] + dfs(i, j + 1)
            if (i + 1) < m:
                down = grid[i][j] + dfs(i + 1, j)
            
            memo[(i, j)] = min(right, down)
            return memo[(i, j)]
        return dfs(0, 0)
        