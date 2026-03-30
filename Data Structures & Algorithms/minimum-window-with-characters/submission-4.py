from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have, required = 0, len(need) 
        
        l, min_len = 0, float('inf')
        res = [0, float('inf')]
        for r in range(len(s)):
            if s[r] in need: 
                need[s[r]] -= 1
                if need[s[r]] == 0:
                    have += 1
            
            while have == required:
                curr_len = r - l + 1
                if curr_len < min_len:
                    min_len = curr_len
                    res = [l, r]
                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        have -= 1
                l += 1
        return s[res[0]:res[1] + 1] if min_len != float('inf') else ""