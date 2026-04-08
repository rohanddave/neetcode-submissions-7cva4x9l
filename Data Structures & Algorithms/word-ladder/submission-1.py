from collections import defaultdict, deque 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        adj = defaultdict(list) 

        for word in wordList: 
            for i in range(L): 
                pattern = word[:i] + "*" + word[i + 1:]
                adj[pattern].append(word) 
        
        print(adj)

        visited = {beginWord}
        q = deque([(beginWord, 1)])

        while q: 
            word, count = q.popleft()
            print(word, count)

            if word == endWord: 
                return count

            for i in range(L):
                pattern = word[:i] + "*" + word[i + 1:]
                for nei in adj[pattern]: 
                    if nei not in visited: 
                        q.append((nei, count + 1))
                        visited.add(nei)
                
        return 0

