class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(i, j):
            count = 0 
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
            return count
        count = 0 
        for i in range(len(s)):
            count += helper(i, i + 1) + helper(i, i)
        return count

        