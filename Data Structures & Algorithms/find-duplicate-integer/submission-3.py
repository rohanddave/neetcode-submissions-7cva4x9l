class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, num in enumerate(nums): 
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            else: 
                nums[idx] *= -1
        return -1
# nums=[1,3,4,2,2]
# nums=[-1,-3,-4,-2,2]

