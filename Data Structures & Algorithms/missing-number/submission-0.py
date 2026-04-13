class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        print(0 ^ 1 ^ 2 ^ 3 ^ 1 ^ 3)
        res = 0
        for i in range(len(nums) + 1): 
            res ^= i
        
        for num in nums:
            res ^= num

        return res

        