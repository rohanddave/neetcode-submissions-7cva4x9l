from collections import defaultdict
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
        # def dfs(i, target, memo = {}): 
        #     if target == 0 and i == len(nums): 
        #         return 1
        #     if target != 0 and i == len(nums):
        #         return 0 
        #     if (i, target) in memo: 
        #         return memo[(i, target)]
            
        #     add = dfs(i + 1, target - nums[i], memo=memo)
        #     subtract = dfs(i + 1, target + nums[i], memo=memo)

        #     memo[(i, target)] = add + subtract 
        #     return memo[(i, target)]
        # return dfs(0, target)
        n = len(nums) 
        dp = [defaultdict(int) for i in range(n + 1)]
        # rows = index; cols = target
        '''
        we start at the base case and move backwards 
        base case is when target == 0 and index == n
        also when index == n row
        so essentially the last row is base case entirely 
        the result will be stored in dp[0][target]

        dp
        '''
        dp[n][0] = 1
        s = sum(nums)
        for i in range(n - 1, -1, -1): 
            for t in range(-s, s + 1): 
                dp[i][t] = dp[i + 1][t - nums[i]] + dp[i + 1][t + nums[i]]
        return dp[0][target]
        