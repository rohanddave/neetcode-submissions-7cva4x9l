from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, curr_prefix_sum, n = 0, 0, len(nums)
        comp_map = defaultdict(int)
        comp_map[0] = 1
        for i in range(n):
            curr_prefix_sum += nums[i]
            complement = curr_prefix_sum - k 
            if complement in comp_map: 
                count += comp_map[complement]
            print(i, curr_prefix_sum, complement, count)
            comp_map[curr_prefix_sum] += 1
        return count
