class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n): 
            dp[i][i] = True
        
        max_len, start = 1, 0
        
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1]:
                max_len = 2
                start = i

        for length in range(3, n + 1): 
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j] and length > max_len: 
                    start = i
                    max_len = length

        return s[start: start + max_len]
        