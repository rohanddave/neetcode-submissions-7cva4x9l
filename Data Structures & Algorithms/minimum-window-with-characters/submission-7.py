from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        required_counts = Counter(t) 
        res_l, res_r, res_len = 0, 0, float('inf')

        def is_valid(counts): 
            for count in counts.values(): 
                if count > 0: 
                    return False 
            return True

        for r in range(len(s)): 
            # expand window by includign character at position r 
            if s[r] in required_counts: 
                required_counts[s[r]] -= 1

            # shirnk window while it is valid
            while is_valid(required_counts):
                # res = min(res, r - l + 1) 
                curr_len = r - l + 1
                if curr_len < res_len: 
                    res_len = curr_len
                    res_l, res_r = l, r

                if s[l] in required_counts: 
                    required_counts[s[l]] += 1
                l += 1
        
        return s[res_l : res_r + 1] if res_len != float('inf') else ""
