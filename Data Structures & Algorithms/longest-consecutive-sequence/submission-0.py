class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0

        for num in nums:
            if num - 1 not in seen:
                curr_len = 1
                while num + curr_len in seen:
                    curr_len += 1
                max_len = max(max_len, curr_len)
        
        return max_len
        