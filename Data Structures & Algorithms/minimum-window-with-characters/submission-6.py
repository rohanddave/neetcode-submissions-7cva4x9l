from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, res = 0, ""
        required_counts = Counter(t) 

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
                curr = s[l : r + 1]
                if not res: 
                    res = curr 
                elif len(curr) < len(res): 
                    res = curr
                if s[l] in required_counts: 
                    required_counts[s[l]] += 1
                l += 1
        
        return res
