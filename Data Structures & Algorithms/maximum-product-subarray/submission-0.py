class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod, max_prod = 1,1
        res = float('-inf')
        for num in nums:
            prev_min, prev_max = min_prod, max_prod 
            min_prod = min(prev_min * num, prev_max * num, num)
            max_prod = max(prev_min * num, prev_max * num, num)
            res = max(res, max_prod)
        return res

        