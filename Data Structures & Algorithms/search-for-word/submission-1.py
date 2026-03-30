class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(r, c, index): 
            if index == len(word):
                return True
            if not (0 <= r < m) or not (0 <= c < n):
                return False 
            if board[r][c] != word[index]:
                return False

            tmp = board[r][c]
            board[r][c] = "#"

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                if dfs(r + dr, c + dc, index + 1):
                    return True

            board[r][c] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True 
        return False
                

        