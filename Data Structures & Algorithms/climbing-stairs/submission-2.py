class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            one = 0 if (i + 1) > n else dp[i + 1]
            two = 0 if (i + 2) > n else dp[i + 2]
            dp[i] = one + two 
        return dp[0]
        