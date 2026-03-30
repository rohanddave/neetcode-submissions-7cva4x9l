class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(r, c, index):
            if index == len(word):
                return True
            # if r < 0 or r >= m or c < 0 or c >= n:
            #     return False 
            # if board[r][c] != word[index]:
            #     return False 

            tmp = board[r][c]
            board[r][c] = "#"
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = r + dr, c + dc
                if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and board[new_r][new_c] == word[index]:
                    if dfs(new_r, new_c, index + 1):
                        return True
            
            board[r][c] = tmp
            return False 
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 1):
                    return True 
        return False
        



        