class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2147483647
        q = collections.deque() 
        for r in range(m):
            for c in range(n): 
                if grid[r][c] == 0: 
                    q.append((r, c, 0))
        
        while q:
            r, c, dist = q.popleft() 

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == INF: 
                    new_dist = dist + 1
                    grid[nr][nc] = new_dist
                    q.append((nr, nc, new_dist))
        

        