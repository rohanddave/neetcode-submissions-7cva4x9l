class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        used = [False] * len(nums)
        def dfs(current):
            if len(current) == len(nums):
                res.append(current[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True 
                current.append(nums[i])
                dfs(current)
                current.pop()
                used[i] = False
        dfs([])
        return res
        