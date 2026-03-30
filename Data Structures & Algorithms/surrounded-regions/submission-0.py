class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs(r,c):
            board[r][c] = '#'

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and board[new_r][new_c] == 'O':
                    dfs(new_r,new_c)
        
        for i in range(m):
            # left border
            if board[i][0] == 'O':
                dfs(i, 0)
            # right border
            if board[i][n-1] == 'O':
                dfs(i, n - 1)
        
        for j in range(n):
            # top border
            if board[0][j] == 'O':
                dfs(0, j)
            # bottom border
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
        