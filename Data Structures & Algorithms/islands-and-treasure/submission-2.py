class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q: 
            x,y,dist = q.popleft()

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 2147483647:
                    grid[new_x][new_y] = dist + 1
                    q.append((new_x,new_y,dist+1))
        

        