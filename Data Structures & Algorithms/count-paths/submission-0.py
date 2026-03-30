class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0 
            
            down = helper(i + 1, j)
            right = helper(i, j + 1)

            return down + right
        return helper(0, 0)
        