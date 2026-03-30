class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0 

        def backtrack(start, current): 
            self.res += current

            for i in range(start, len(nums)):
                tmp = current 
                current ^= nums[i]
                backtrack(i + 1, current)
                current = tmp 
        backtrack(0, 0)
        return self.res
        