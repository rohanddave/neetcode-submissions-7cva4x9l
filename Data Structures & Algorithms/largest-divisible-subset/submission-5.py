class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # memo = {}
        # def dfs(i, j): 
        #     if i == len(nums):
        #         return []
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     pick = []
        #     if j == -1 or nums[i] % nums[j] == 0:
        #         pick = [nums[i]] + dfs(i + 1, i)
        #     skip = dfs(i + 1, j)

        #     memo[(i, j)] = pick if len(pick) > len(skip) else skip
        #     return memo[(i, j)]
        # return dfs(0, -1)
        nums.sort()
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        # rows => i and cols => j
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                skip = dp[i + 1][j + 1]
                pick = 0
                if j == -1 or nums[i] % nums[j] == 0:
                    pick = 1 + dp[i + 1][i + 1]
                dp[i][j + 1] = max(pick, skip)

        res = [] 
        i, j = 0, -1

        while i < n:
            skip = dp[i + 1][j + 1]
            pick = 0

            if j == -1 or nums[i] % nums[j] == 0:
                pick = 1 + dp[i + 1][i + 1]

            if pick > skip:
                res.append(nums[i])
                j = i
            i += 1

        return res
        