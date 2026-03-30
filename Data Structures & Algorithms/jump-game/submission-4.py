# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         required = [len(nums) - i - 1 for i in range(len(nums))]

#         i = 0
#         while i < len(nums) and nums[i] != 0:
#             for max_jump in range(nums[i], -1, -1):
#             # max_jump = nums[i]
#             # while True: 
#                 new_index = i + max_jump
#                 if nums[new_index] == required[new_index]:
#                     break
#                 else:
#                     max_jump -= 1
#             # while max_jump > nums[i] and nums[i + max_jump] >= required[i + max_jump]: 
#             #     max_jump -= 1
#             i += max_jump
#         return i >= len(nums) - 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i in range(len(nums)):
            if i > furthest:  # If current index is beyond the furthest reachable index, we can't proceed
                return False
            furthest = max(furthest, i + nums[i])  # Update the furthest reachable point
        return furthest >= len(nums) - 1  # Check if we can reach or exceed the last index