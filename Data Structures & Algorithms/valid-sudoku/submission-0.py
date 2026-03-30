class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(0, 9):
            for j in range(0, 9):
                char = board[i][j]
                if char != ".":
                    if char in rows[i] or char in cols[j] or char in grids[i//3][j//3]:
                        return False
                    else: 
                        rows[i].add(char)
                        cols[j].add(char)
                        grids[i//3][j//3].add(char)
        return True