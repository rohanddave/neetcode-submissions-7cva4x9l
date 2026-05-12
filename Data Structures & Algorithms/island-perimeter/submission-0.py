from collections import deque 
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        1 -> land and 0 -> water 
        cells are connected horizontally and vertically 
        grid is surrounded by water 
        exactly one island 
        island has no "lakes" 
        find the perimeter of the island 

        find the first 1 and perform bfs from there to find all cells 
        of the island 

        the contribution of one cell to perimeter is the number 
        of neighboring water cells 
        '''
        m, n = len(grid), len(grid[0])

        def find_perimeter(i, j): 
            visited = {(i, j)} 
            q = deque([(i ,j)]) 
            perimeter = 0

            while q: 
                r, c = q.popleft()
                perimeter_contribution = 4

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1: 
                        perimeter_contribution -= 1
                        if (nr, nc) not in visited: 
                            visited.add((nr, nc))
                            q.append((nr, nc))

                perimeter += perimeter_contribution            
            return perimeter

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1: 
                    return find_perimeter(i, j)
        return -1



        