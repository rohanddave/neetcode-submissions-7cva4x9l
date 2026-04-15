from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        required_counts, window = Counter(t), defaultdict(int)
        have, required_count = 0, len(required_counts)

        res_l, res_r, res_len = 0, 0, float('inf')

        for r in range(len(s)): 
            # expand window by includign character at position r 
            window[s[r]] += 1
            if s[r] in required_counts and window[s[r]] == required_counts[s[r]]:
                have += 1

            # shirnk window while it is valid
            while have == required_count:
                curr_len = r - l + 1
                if curr_len < res_len: 
                    res_len = curr_len
                    res_l, res_r = l, r
                
                window[s[l]] -= 1
                if s[l] in required_counts and window[s[l]] < required_counts[s[l]]:
                    have -= 1
                l += 1
        
        return s[res_l : res_r + 1] if res_len != float('inf') else ""
