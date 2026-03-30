class Node: 
    def __init__(self, key: str, isEnd: bool = False):
        self.key = key
        self.children = [None] * 26
        self.isEnd = isEnd

class PrefixTree:

    def __init__(self):
        self.root = Node('#')
    
    def char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.children[self.char_to_index(char)]:
                curr.children[self.char_to_index(char)] = Node(char)
            curr = curr.children[self.char_to_index(char)]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not curr.children[self.char_to_index(char)]:
                return False
            curr = curr.children[self.char_to_index(char)]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.children[self.char_to_index(char)]:
                return False
            curr = curr.children[self.char_to_index(char)]
        if curr:
            return True
        return False
        
        