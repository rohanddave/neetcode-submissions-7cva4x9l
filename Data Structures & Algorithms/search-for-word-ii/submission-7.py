class TrieNode: 
    def __init__(self, val):
        self.word = None 
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
                        node.word = word
                    curr = node                   
        
        res = []
        m, n = len(board), len(board[0])
        build_trie(head, words)

        def dfs(r, c, curr_trie): 
            if not (0 <= r < m and 0 <= c < n):
                return
            
            if curr_trie.word: 
                res.append(curr_trie.word)
                curr_trie.word = None

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#' and curr_trie.children[ord(board[nr][nc]) - ord('a')]:
                    temp = board[nr][nc] 
                    board[nr][nc] = '#'
                    dfs(nr, nc, curr_trie.children[ord(temp) - ord('a')])
                    board[nr][nc] = temp
        for r in range(m):
            for c in range(n):
                curr, char = head, board[r][c]
                if char != '#' and curr.children[ord(char) - ord('a')]:
                    board[r][c] = "#"
                    dfs(r, c, curr.children[ord(char) - ord('a')])
                    board[r][c] = char
        return res