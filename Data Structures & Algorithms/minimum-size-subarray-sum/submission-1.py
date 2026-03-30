class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, res = 0, float('inf')
        window_sum = 0 

        for right in range(len(nums)):
            window_sum += nums[right]

            while left <= right and window_sum >= target: 
                res = min(res, right - left + 1) 
                window_sum -= nums[left]
                left += 1

        return 0 if res == float('inf') else res