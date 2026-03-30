from collections import deque 

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        q = deque() 

        for i in range(n): 
            if board[i][0] == 'O': 
                q.append((i, 0))
            if board[i][m - 1] == 'O': 
                q.append((i, m - 1))
        
        for j in range(m): 
            if board[0][j] == 'O': 
                q.append((0, j))
            if board[n - 1][j] == 'O':
                q.append((n - 1, j))

        while q: 
            r, c = q.popleft() 

            board[r][c] = 'Z'

            for dr, dc in [(1,0),(-1,0),(0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'O': 
                    q.append((nr, nc))
        

        for i in range(n): 
            for j in range(m): 
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(n): 
            for j in range(m): 
                if board[i][j] == 'Z': 
                    board[i][j] = 'O'
        
        