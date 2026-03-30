class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums)):
            num = nums[i]
            if i != 0 and nums[i-1] == nums[i]:
                continue
            l = i + 1
            r = len(nums) - 1
            threeSum = nums[i]
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r = r - 1
                elif threeSum < 0:
                    l = l + 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result

                
        