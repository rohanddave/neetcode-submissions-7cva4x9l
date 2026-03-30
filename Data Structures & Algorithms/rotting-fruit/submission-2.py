class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        print(m, n)
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        minutes = 0
        while q: 
            x, y, curr_min = q.popleft()
            minutes = max(minutes, curr_min)

            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1: 
                    grid[new_x][new_y] = 2
                    q.append((new_x,new_y,curr_min+1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutes
        
        