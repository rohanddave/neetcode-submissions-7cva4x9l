class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele, freq = nums[0], 1
        for i in range(1, len(nums)): 
            freq += 1 if nums[i] == ele else -1
            if freq == 0: 
                ele = nums[i]
                freq = 1
        return ele
        