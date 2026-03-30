class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False 
        target_partition_sum = total_sum // 2
        def dfs(i, target): 
            if target == 0:
                return True 
            if target < 0:
                return False
            if i >= len(nums):
                return False
            
            include = dfs(i + 1, target - nums[i])
            exclude = dfs(i + 1, target)
            
            return include or exclude
        return dfs(0, target_partition_sum)
            

        