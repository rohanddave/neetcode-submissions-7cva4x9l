class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []
        for i in range(len(nums)): 
            if i != 0 and nums[i] == nums[i - 1]: 
                continue 
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r: 
                s = nums[l] + nums[r]
                if s < target: 
                    l += 1
                elif s > target: 
                    r -= 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]: 
                        r -= 1
        return res


        