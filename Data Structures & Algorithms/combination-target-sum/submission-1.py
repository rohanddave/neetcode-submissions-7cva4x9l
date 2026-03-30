class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = [] 
        nums.sort()

        def backtrack(start, current, remaining): 
            if remaining == 0:
                self.res.append(current[:])
                return 
            
            for i in range(start, len(nums)): 
                if nums[i] > remaining:
                    break
                current.append(nums[i])
                backtrack(i, current, remaining - nums[i])
                current.pop()
        backtrack(0, [], target)
        return self.res
                 
                
        