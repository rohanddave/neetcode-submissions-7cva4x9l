class TrieNode: 
    def __init__(self, val):
        self.val = val 
        self.children = {} 
        self.is_end = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode('')
        
        for word in strs: 
            curr = root 
            for char in word: 
                if char not in curr.children: 
                    curr.children[char] = TrieNode(char)
                curr = curr.children[char]
            curr.is_end = True
        
        curr = root
        res = ''
        while len(curr.children) == 1 and not curr.is_end: 
            char, node = curr.children.popitem()
            curr = node
            res += char
        return res

        
                

        