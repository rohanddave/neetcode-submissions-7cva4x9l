class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(i, j): 
            while i >= 0 and j < len(s) and s[i] == s[j]: 
                i -= 1
                j += 1
            # start inclusive, end exclusive: [start, end)
            return s[i + 1: j]
        
        res = '' 

        for i in range(len(s)): 
            even, odd = expand_around_center(i, i + 1), expand_around_center(i, i)
            if len(even) > len(res): 
                res = even
            if len(odd) > len(res): 
                res = odd
        return res

        