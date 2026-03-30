class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set() 
        neg_diag = set() 
        res = [] 
        board = [['.'] * n for _ in range(n)]

        def dfs(row, board):
            # some base case here 
            if row == n:
                res.append([''.join(r) for r in board])
                return 
            
            for j in range(n): 
                if j in cols or (row - j) in neg_diag or (row + j) in pos_diag:
                    continue
                
                cols.add(j)
                pos_diag.add(row + j)
                neg_diag.add(row - j)
                board[row][j] = "Q"

                dfs(row + 1, board)

                cols.remove(j)
                pos_diag.remove(row + j)
                neg_diag.remove(row - j)
                board[row][j] = "."
        dfs(0, board)

        return res
        