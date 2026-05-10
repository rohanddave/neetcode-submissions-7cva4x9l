class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        memo = {}
        def dfs(r, c):
            if r == height - 1:
                return triangle[r][c]
            if (r, c) in memo:
                return memo[(r, c)]
            
            option_1 = triangle[r][c] + dfs(r + 1, c)
            option_2 = triangle[r][c] + dfs(r + 1, c + 1)
            memo[(r, c)] = min(option_1, option_2)
            return memo[(r, c)]
        return dfs(0, 0)
