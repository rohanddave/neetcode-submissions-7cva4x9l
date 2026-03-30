class Node:
    def __init__(self, key: str, isEnd: bool = False):
        self.key = key
        self.children = [None] * 26
        self.isEnd = isEnd
    
class WordDictionary:

    def __init__(self):
        self.root = Node('#')
    
    def char_to_index(self, char):
        return ord(char) - ord('a')

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word: 
            if not curr.children[self.char_to_index(char)]:
                curr.children[self.char_to_index(char)] = Node(char)
            curr = curr.children[self.char_to_index(char)]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.subtreeSearch(word, self.root)
        # for char in word: 
        #     if char == '.':
        #         stack = []
        #         # finding all possible non null children
        #         for child in curr.children:
        #             if child:
        #                 stack.append(child)
                
        #         while stack: 

        #     else:
        #         if not curr.children[self.char_to_index(char)]:
        #             return False
        #         curr = curr.children[self.char_to_index(char)]
        # return (curr and curr.isEnd)


    def subtreeSearch(self, word: str, node) -> bool:
        if not word and node.isEnd:
            return True
        curr = node
        for i in range(0, len(word)):
            char = word[i]
            if char == '.':
                stack = []
                # finding all possible non null children
                for child in curr.children:
                    if child:
                        stack.append(child)
                
                while stack:
                    res = self.subtreeSearch(word[i + 1:], stack.pop())
                    if res:
                        return True
                return False

            else:
                if not curr.children[self.char_to_index(char)]:
                    return False
                curr = curr.children[self.char_to_index(char)]
        return (curr and curr.isEnd)

        
