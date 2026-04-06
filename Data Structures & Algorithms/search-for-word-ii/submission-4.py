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
        visited = set()
        m, n = len(board), len(board[0])
        build_trie(head, words)

        def dfs(r, c, curr_word, curr_trie): 
            if not (0 <= r < m and 0 <= c < n):
                return
            
            if curr_trie.is_end: 
                res.append("".join(curr_word))
                curr_trie.is_end = False
                # print(f'printing visited when found word {word_string}: {visited}')
                # return True

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited and curr_trie.children[ord(board[nr][nc]) - ord('a')]:
                    curr_word.append(board[nr][nc])
                    visited.add((nr, nc))
                    dfs(nr, nc, curr_word, curr_trie.children[ord(board[nr][nc]) - ord('a')])
                    visited.remove((nr, nc))
                    curr_word.pop()
        for r in range(m):
            for c in range(n): 
                # print('starting dfs at: ', (r, c))
                curr, char = head, board[r][c]
                if curr.children[ord(char) - ord('a')]:
                    visited.add((r,c))
                    dfs(r, c, [char], curr.children[ord(char) - ord('a')])
                    visited.remove((r,c))
        # print(res)
        return res