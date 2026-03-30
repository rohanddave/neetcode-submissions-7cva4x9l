class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs_linear(linear):
            memo = {}
            def dfs(i):
                if i >= len(linear):
                    return 0 
                if i in memo:
                    return memo[i]
                
                rob = linear[i] + dfs(i + 2)
                skip = dfs(i + 1)
                memo[i] = max(rob, skip)
                return memo[i]
            return dfs(0)
        return max(dfs_linear(nums[1:]), dfs_linear(nums[:-1]))
                
                
        