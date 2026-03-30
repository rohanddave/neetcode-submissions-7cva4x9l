class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        seen = set()

        def dfs(i, j, curr):
            if curr == word:
                return True

            if i < 0 or j < 0 or i >= rows or j >= cols or len(curr) > len(word) or (i,j) in seen:
                return False
            
            seen.add((i, j))
            last_index = len(curr)
            res = dfs(i, j - 1, curr + board[i][j]) or dfs(i, j + 1, curr + board[i][j]) or dfs(i - 1, j, curr + board[i][j]) or dfs(i + 1, j, curr + board[i][j])
            seen.remove((i,j))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c, ""): return True
        return False
        