from collections import deque 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = set() 
        
        def bfs(i ,j): 
            q = deque([(i, j)])
            visited.add((i, j))
            region = set()

            def is_edge(i, j): 
                return not ((1 <= i < m - 1) and (1 <= j < n - 1))

            if not is_edge(i, j):
                region.add((i, j))

            is_surrounded = not is_edge(i, j)

            while q: 
                r, c = q.popleft() 

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and board[nr][nc] == 'O': 
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        if not is_edge(nr, nc):
                            region.add((nr, nc))
                        is_surrounded = is_surrounded and not is_edge(nr, nc)
            
            if is_surrounded: 
                for r, c in region: 
                    board[r][c] = 'X'


        for i in range(m): 
            for j in range(n): 
                if board[i][j] == 'O' and (i, j) not in visited: 
                    bfs(i, j)
        
        