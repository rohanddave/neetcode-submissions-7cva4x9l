class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = set() 
        max_area = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in visited:
                return 0
            
            visited.add((i, j))  # Correctly mark (i, j) as visited
            area = 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == 1 and (nx, ny) not in visited: 
                    area += dfs(nx, ny)  # Accumulate area
            return area

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in visited:
                    max_area = max(dfs(x, y), max_area)
        
        return max_area