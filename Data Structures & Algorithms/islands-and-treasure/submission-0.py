from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid) 
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        treasures = []

        for x in range (m):
            for y in range(n):
                if grid[x][y] == 0:
                    treasures.append((x, y))
        
        for treasure in treasures:
            q = deque([(treasure[0], treasure[1], 0)])
            visited = set() 
            while q:
                x, y, distance = q.popleft() 
                visited.add((x, y))
                grid[x][y] = min(grid[x][y], distance)
                for dx, dy in directions: 
                    nx, ny = x + dx, y + dy
                    if nx >= 0 and nx < m and ny >=0 and ny < n and (nx, ny) not in visited and grid[nx][ny] != -1 and grid[nx][ny] != 0: 
                        q.append((nx, ny, distance + 1))
            



        