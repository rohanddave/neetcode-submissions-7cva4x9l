class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        we want to divide the array into two halves such that sum(half1) == sum(half2)
        since we want only two subsets then the sum(half1) == sum(total) / 2
        if the sum is odd then return false 
        if the sum is even try making a sum of total / 2 
        at each point we decide if we want to include or exclude the current number 
        this then becomes a target sum problem where the target = total / 2
        '''

        total = sum(nums)

        if total % 2 != 0: 
            return False 
        
        memo = {} 
        def dfs(i, target):
            if target == 0: 
                return True 
            if i == len(nums):
                return False 
            if (i, target) in memo:
                return memo[(i, target)]
            
            include = dfs(i + 1, target - nums[i])
            exclude = dfs(i + 1, target)

            memo[(i, target)] = include or exclude 
            return memo[(i, target)]
        return dfs(0, total / 2)

        