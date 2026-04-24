class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [] 
        def dfs(i, current): 
            self.res.append(current[:])

            for i in range(i, len(nums)): 
                current.append(nums[i])
                dfs(i + 1, current)
                current.pop()
        dfs(0, [])
        return self.res

        