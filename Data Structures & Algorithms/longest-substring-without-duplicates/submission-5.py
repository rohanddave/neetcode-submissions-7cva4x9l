class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        l, max_len = 0, 0
        for r in range(len(s)):
            # shrink to a valid window
            if s[r] in window and window[s[r]] >= l: 
                l = window[s[r]] + 1
            
            # expand window
            window[s[r]] = r
            max_len = max(max_len, r - l + 1)
        return max_len
