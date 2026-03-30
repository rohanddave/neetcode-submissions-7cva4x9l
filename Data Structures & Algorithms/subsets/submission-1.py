class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [] 

        def backtrack(start, current): 
            self.res.append(current[:])

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        backtrack(0, [])
        return self.res

        