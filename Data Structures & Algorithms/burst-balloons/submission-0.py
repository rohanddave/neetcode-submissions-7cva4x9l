class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            res = 0
            for i in range(l, r + 1):
                prev = nums[l - 1] if l - 1 >= 0 else 1
                nex = nums[r + 1] if r + 1 < len(nums) else 1
                curr_contr = nums[i] * prev * nex
                res = max(res, curr_contr + dfs(l, i - 1) + dfs(i + 1, r))
            
            memo[(l, r)] = res
            return memo[(l, r)]
        return dfs(0, len(nums) - 1)