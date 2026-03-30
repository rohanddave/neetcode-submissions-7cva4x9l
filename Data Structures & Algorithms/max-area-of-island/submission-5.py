class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    q = collections.deque([(i,j)])
                    grid[i][j] = 0
                    area = 0
                    while q: 
                        x, y = q.popleft() 
                        area += 1

                        for dx, dy in [(1, 0), (-1, 0), (0, 1),(0, -1)]:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                                grid[new_x][new_y] = 0 
                                q.append((new_x, new_y))
                    max_area = max(area, max_area)
        
        return max_area
        