class TrieNode: 
    def __init__(self, val):
        self.is_end = False 
        self.val =  val 
        self.children = [None] * 26

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = TrieNode('')
        def build_trie(head, words): 
            for word in words: 
                curr = head 
                for i, char in enumerate(word): 
                    node = None
                    if curr.children[ord(char) - ord('a')]:
                        node = curr.children[ord(char) - ord('a')]
                    else:
                        node = TrieNode(char)
                        curr.children[ord(char) - ord('a')] = node
                    
                    if i == len(word) - 1:
                        node.is_end = True
                    curr = node                   
        
        res = []
        m, n = len(board), len(board[0])
        build_trie(head, words)

        def dfs(r, c, curr_word, curr_trie): 
            if not (0 <= r < m and 0 <= c < n):
                return
            
            if curr_trie.is_end: 
                res.append("".join(curr_word))
                curr_trie.is_end = False

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#' and curr_trie.children[ord(board[nr][nc]) - ord('a')]:
                    curr_word.append(board[nr][nc])
                    temp = board[nr][nc] 
                    board[nr][nc] = '#'
                    dfs(nr, nc, curr_word, curr_trie.children[ord(temp) - ord('a')])
                    board[nr][nc] = curr_word.pop()
        for r in range(m):
            for c in range(n):
                curr, char = head, board[r][c]
                if char != '#' and curr.children[ord(char) - ord('a')]:
                    board[r][c] = "#"
                    dfs(r, c, [char], curr.children[ord(char) - ord('a')])
                    board[r][c] = char
        return res