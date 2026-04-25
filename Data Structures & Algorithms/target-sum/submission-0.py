class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, target): 
            if target == 0 and i == len(nums): 
                return 1
            if i >= len(nums):
                return 0
            
            # add number 
            add = dfs(i + 1, target - nums[i])
            # subtract number 
            subtract = dfs(i + 1, target + nums[i])

            return add + subtract 
        return dfs(0, target)
        