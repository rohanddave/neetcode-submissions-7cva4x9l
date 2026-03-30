class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1: 
            if c in count.keys():
                count[c] += 1
            else:
                count[c] = 1
        
        for l in range(0, len(s2)):
            if s2[l] in count.keys():
                # first character of window matches
                r = l
                window_count = {}
                # window_count[s2[l]] = -1
                while r < len(s2) and r - l < len(s1) and s2[r] in count.keys():
                    if s2[r] in window_count.keys():
                        window_count[s2[r]] -= 1
                    else:
                        window_count[s2[r]] = -1
                    r += 1
                didFindSubstring = True
                for key in count.keys():
                    if key not in window_count.keys() or window_count[key] + count[key] != 0:
                        didFindSubstring = False
                        break
                if didFindSubstring: 
                    return True
                
        return False
        