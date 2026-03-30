class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = [] 

        def dfs(start, current, remaining):
            if remaining == 0:
                self.res.append(current[:])
                return 
            
            for i in range(start, len(nums)):
                if nums[i] > remaining: 
                    continue
                current.append(nums[i])
                dfs(i, current, remaining - nums[i])
                current.pop()
        dfs(0, [], target)
        return self.res
        