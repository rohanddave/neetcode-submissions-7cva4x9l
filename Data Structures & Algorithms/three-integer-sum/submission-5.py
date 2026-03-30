class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n, res = len(nums), []

        for i in range(n):
            if i != 0 and nums[i] == nums[i -1]:
                continue
            target = -nums[i] 
            l, r = i + 1, n - 1
            while l < r:
                left, right = nums[l], nums[r]
                curr_sum = left + right
                if curr_sum < target: 
                    l += 1
                elif curr_sum > target: 
                    r -= 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == left: 
                        l += 1
                    while r > l and nums[r] == right: 
                        r -= 1
        return res