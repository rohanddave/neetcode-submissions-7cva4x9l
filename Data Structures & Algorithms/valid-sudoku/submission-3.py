class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [True] * 9
        cols = [True] * 9
        grids = [[True] * 3] * 3

        seen_row = [set() for _ in range(9)]
        seen_col = [set() for _ in range(9)]
        seen_grid = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == '.':
                    continue
                
                if board[row][col] in seen_row[row] or board[row][col] in seen_col[col] or board[row][col] in seen_grid[row // 3][col // 3]:
                    return False

                seen_row[row].add(board[row][col])
                seen_col[col].add(board[row][col])
                seen_grid[row // 3][col // 3].add(board[row][col])
                
        return True
                
                

