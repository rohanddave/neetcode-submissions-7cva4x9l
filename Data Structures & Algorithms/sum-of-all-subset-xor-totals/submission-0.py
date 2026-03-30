class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # self.res = []
        self.res = 0

        def backtrack(start, current): 
            self.res += current 
            # self.res.append(current[:])

            for i in range(start, len(nums)):
                tmp = current 
                current ^= nums[i]
                # current.append(nums[i])
                backtrack(i + 1, current)
                current = tmp
                # current.pop()
        backtrack(0, 0)
        # print(self.res)
        return self.res
        