class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        build expression using ALL numbers in nums that sums to target 
        can use + or - with each num 

        decision at each number is if: + or - 

        do a top down dfs passing current index and target sum
        base case 1: if target == 0 and i == len(nums) -> return 1
        base case 2: if i == len(nums) return 0

        res = nums[0] - nums[1] 
        remaining = target - res 

        decision +: dfs(i + 1, target - nums[i])
        decision -: dfs(i + 1, target + nums[i])
        '''
        def dfs(i, target, memo = {}): 
            if target == 0 and i == len(nums): 
                return 1
            if target != 0 and i == len(nums):
                return 0 
            if (i, target) in memo: 
                return memo[(i, target)]
            
            add = dfs(i + 1, target - nums[i], memo=memo)
            subtract = dfs(i + 1, target + nums[i], memo=memo)

            memo[(i, target)] = add + subtract 
            return memo[(i, target)]
        return dfs(0, target)
        