from collections import defaultdict, deque 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_diff(a, b): 
            n = len(a)
            diff = 0 

            for i in range(n): 
                if a[i] != b[i]:
                    diff += 1
            return diff
        
        adj = defaultdict(list)
        
        for i in range(len(wordList)): 
            for j in range(i + 1, len(wordList)):
                # think about what happens when the words are equal
                if get_diff(wordList[i], wordList[j]) == 1: 
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        for i in range(len(wordList)):
            if get_diff(beginWord, wordList[i]) == 1: 
                adj[wordList[i]].append(beginWord)
                adj[beginWord].append(wordList[i])
        


        visited = {beginWord}
        q = deque([(beginWord, 1)])

        while q: 
            word, count = q.popleft()
            print(word, count)

            if word == endWord: 
                return count

            for nei in adj[word]: 
                if nei not in visited: 
                    q.append((nei, count + 1))
                    visited.add(nei)
        return 0

