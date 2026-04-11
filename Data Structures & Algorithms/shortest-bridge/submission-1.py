class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 
        visited = set()
        exploration_q = deque()

        def explore_island(i, j): 
            q = deque([(i,j)]) 
            visited.add((i,j))

            while q: 
                r, c = q.popleft() 

                exploration_q.append((r, c, 0))

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1: 
                        q.append((nr, nc))
                        visited.add((nr, nc))


        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1 and (i, j) not in visited: 
                    explore_island(i, j)
                    while exploration_q: 
                        r, c, dist = exploration_q.popleft() 

                        for dr, dc in  [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc 
                            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                                if grid[nr][nc] == 1: 
                                    return dist
                                exploration_q.append((nr, nc, dist + 1))
                                visited.add((nr, nc))
        return -1

