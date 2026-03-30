# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         i, j = 0, len(nums) - 1
#         curr_sum = sum(nums)
#         max_sum = curr_sum
#         while i < j:
#             if curr_sum - nums[i] >= curr_sum - nums[j]:
#                 curr_sum -= nums[i]
#                 i += 1
#             else:
#                 curr_sum -= nums[j]
#                 j -= 1
#             max_sum = max(max_sum, curr_sum)
#         return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Continue with the current subarray or start a new one
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater
        
        return max_sum