from collections import deque 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque() 
        visited = set()

        def is_edge(i, j): 
            return not ((1 <= i < m - 1) and (1 <= j < n - 1))

        for i in range(m): 
            for j in range(n): 
                if board[i][j] == 'O' and is_edge(i, j): 
                    q.append((i, j))
                    visited.add((i, j))
        
        while q: 
            r, c = q.popleft() 

            board[r][c] = 'Z'

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and board[nr][nc] == 'O': 
                    q.append((nr, nc))
                    visited.add((nr, nc))

        for i in range(m):
            for j in range(n): 
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Z': 
                    board[i][j] = 'O'
        
        # for i in range(m): 
        #     for j in range(n): 
        #         if board[i][j] == 'Z':
        #             board[i][j] = 'O'