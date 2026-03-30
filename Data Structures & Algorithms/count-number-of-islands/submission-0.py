from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set() 
        count = 0

        for i in range(m):
            for j in range(n): 
                if (i, j) not in visited and grid[i][j] == '1': 
                    count += 1
                    q = deque([(i, j)])
                    visited.add((i,j))
                    while q: 
                        x, y = q.popleft() 
                        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            new_x, new_y = x + dx, y + dy 
                            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == '1':
                                q.append((new_x,new_y))
                                visited.add((new_x,new_y))
        return count

        