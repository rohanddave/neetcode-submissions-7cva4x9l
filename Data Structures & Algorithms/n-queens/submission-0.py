class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        cols = set() 
        pos_diag = set() 
        neg_diag = set() 


        def dfs(row, board):
            if row == n:
                self.res.append([''.join(r) for r in board])
                return 
            
            for j in range(n):
                if j in cols or (row - j) in neg_diag or (row + j) in pos_diag: 
                    continue 
                
                # choose
                cols.add(j)
                neg_diag.add(row - j)
                pos_diag.add(row + j)
                board[row][j] = "Q"

                dfs(row + 1, board)

                # backtrack
                cols.remove(j)
                neg_diag.remove(row - j)
                pos_diag.remove(row + j)
                board[row][j] = "."
        board = [['.' ] * n for _ in range(n)]
        dfs(0, board)
        return self.res