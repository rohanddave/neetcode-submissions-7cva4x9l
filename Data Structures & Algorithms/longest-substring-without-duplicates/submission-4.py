class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set() 
        l, max_len = 0, 0
        for r in range(len(s)):
            # shrink to a valid window
            while s[r] in window: 
                window.remove(s[l])
                l += 1
            
            # expand window
            window.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len
