class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, result = 0, 1
        seen = set()
        seen.add(s[0])
        for r in range(1, len(s)):
            if s[r] in seen:
                while l < r and s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                result = max(result, r - l + 1)
            # else:÷
            seen.add(s[r])
            result = max(result, r - l + 1)
        return result

                    

