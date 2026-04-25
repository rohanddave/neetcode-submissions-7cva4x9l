class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} 
        def dfs(i, target): 
            if target == 0 and i == len(nums): 
                return 1
            if i >= len(nums):
                return 0
            if (i, target) in memo:
                return memo[(i, target)]
            
            # add number 
            add = dfs(i + 1, target - nums[i])
            # subtract number 
            subtract = dfs(i + 1, target + nums[i])

            memo[(i, target)] = add + subtract 
            return memo[(i, target)]
        return dfs(0, target)
        