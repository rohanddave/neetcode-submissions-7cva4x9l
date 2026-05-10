from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = Counter(s) 
        for char in t: 
            if char not in count:
                return False 
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        return True if not count else False