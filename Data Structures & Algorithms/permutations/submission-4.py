class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.used = [False] * n 
        self.res = []

        def dfs(current): 
            if len(current) == n:
                self.res.append(current[:])
                return
            
            for i in range(n): 
                if self.used[i]:
                    continue
                
                current.append(nums[i])
                self.used[i] = True
                dfs(current)
                current.pop()
                self.used[i] = False
        dfs([])
        return self.res

        