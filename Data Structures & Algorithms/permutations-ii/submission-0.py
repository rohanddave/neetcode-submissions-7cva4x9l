class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = [] 
        nums.sort()
        self.used = [False] * len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                self.res.append(current[:])
                return 
            
            for i in range(len(nums)):
                if self.used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                    continue 
                
                self.used[i] = True 
                current.append(nums[i])
                backtrack(current)
                current.pop()
                self.used[i] = False
        backtrack([])
        return self.res
        