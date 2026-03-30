class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            num = nums[i]
            remaining = target - num
            l = i + 1 if remaining > num else 0
            r = len(nums) - 1 if remaining > num else i - 1
            while l >= 0 and r < len(nums) and l <= r:
                mid = (l + r) // 2
                if nums[mid] == remaining:
                    return [i + 1, mid + 1]
                elif remaining < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return []

        