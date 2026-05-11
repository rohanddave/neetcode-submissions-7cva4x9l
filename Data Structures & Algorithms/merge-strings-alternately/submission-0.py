class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        res = []
        while p1 < len(word1) and p2 < len(word2): 
            res.append(word1[p1])
            res.append(word2[p2])
            p1 += 1
            p2 += 1
        
        if p1 < len(word1):
            res.extend(word1[p1:])
        if p2 < len(word2): 
            res.extend(word2[p2:])
        return ''.join(res)
        
            

        