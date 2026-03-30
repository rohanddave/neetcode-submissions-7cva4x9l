class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [float('inf')] * len(nums)
        res[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            j = nums[i]
            while j > 0:
                if i + j < len(nums):
                    res[i] = min(res[i + j] + 1, res[i])
                j-= 1

        return res[0]
        