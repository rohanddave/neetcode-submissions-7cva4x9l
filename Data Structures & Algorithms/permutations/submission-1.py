class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False] * len(nums)

        def backtrack(current): 
            if len(current) == len(nums):
                self.res.append(current[:])
                return 
            
            for i in range(len(nums)):
                if self.used[i]:
                    continue
                self.used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                self.used[i] = False
        backtrack([])
        return self.res
            
        