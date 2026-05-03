'''
nums[i] = money ith house has 
houses are in a straight line 
ith house is the neighbor of i-1 and i + 1 house 
return max amount of money without robbing two adjacent houses 

state: current house we're at 
invariant: cannot rob two adjacent houses 
decision: rob / don't rob 
dfs function returns the max amount that can be robbed at the ith house
if 
'''

'''
at the ith house the decision to rob or skip depends on the i + 1 and i + 2 house 

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        for i in range(len(nums) - 1, -1, -1): 
            rob = nums[i] + dp[i + 2]
            skip = dp[i + 1]
            dp[i] = max(rob, skip)
        return dp[0]
        # memo = {}
        # def dfs(i): 
        #     if i >= len(nums):
        #         return 0
        #     if i in memo:
        #         return memo[i]
            
        #     rob = nums[i] + dfs(i + 2)
        #     skip = dfs(i + 1)

        #     memo[i] = max(rob, skip)
        #     return memo[i]
        
        # return dfs(0)

        