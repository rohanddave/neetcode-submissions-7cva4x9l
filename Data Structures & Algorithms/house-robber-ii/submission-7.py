class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 
        if n == 1:
            return nums[0]
        memo = {}
        def dfs_linear(start, end):
            memo = {}
            def dfs(i): 
                if i >= end:
                    return 0
                if i in memo: 
                    return memo[i]
                
                steal = nums[i] + dfs(i + 2)
                skip = dfs(i + 1)

                memo[i] = max(steal, skip)
                return memo[i]
            return dfs(start)
        return max(dfs_linear(0, n - 1), dfs_linear(1, n))
        