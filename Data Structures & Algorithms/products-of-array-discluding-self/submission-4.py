class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        postfix = [1] * length
        res = []

        for i in range(1, length):
            prefix[i] *= prefix[i - 1] * nums[i - 1]
            postfix[length - i - 1] *= postfix[length - i] * nums[length - i]

        for i in range(0, length):
            res.append(postfix[i] * prefix[i])
        
        return res