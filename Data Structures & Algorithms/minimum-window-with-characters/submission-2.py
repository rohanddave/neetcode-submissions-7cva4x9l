class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for char in t: 
            freq[char] = freq.get(char, 0) + 1
    
        required = len(t)

        res = ""
        l = 0
        for r in range(len(s)): 
            char = s[r]
            if char in freq: 
                if freq[char] > 0:
                    required -= 1
                freq[char] -= 1
 
            # shrink window 
            while required == 0:
                if res == "" or (r - l + 1) < len(res):
                    res = s[l:r+1]

                if s[l] in freq:
                    freq[s[l]] += 1
                    if freq[s[l]] > 0:
                        required += 1
                l += 1
            
        return res
