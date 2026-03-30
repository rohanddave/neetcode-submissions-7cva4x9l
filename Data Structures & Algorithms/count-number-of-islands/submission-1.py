from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set() 
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    q = deque([(i, j)])
                    visited.add((i,j))
                    while q: 
                        x, y = q.popleft() 
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == '1':
                                visited.add((new_x, new_y))
                                q.append((new_x, new_y))
                    count += 1
        
        return count



        