class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], (nums[i] + dp[i + 2]))
        return dp[0]
        # memo = {}
        # def dfs(i): 
        #     if i >= n: 
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     steal = nums[i] + dfs(i + 2) 
        #     skip = dfs(i + 1) 
        #     memo[i] = max(steal, skip)
        #     return memo[i]
        # return dfs(0)
        