class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        # visited = set() 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))
                    # visited.add((i,j))
        
        while q: 
            x,y,dist = q.popleft()
            print(x,y,dist)
            # if grid[x][y] == float('inf'):
            #     grid[x][y] = dist + 1

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 2147483647:
                    # visited.add((new_x, new_y))
                    grid[new_x][new_y] = dist + 1
                    q.append((new_x,new_y,dist+1))
        

        