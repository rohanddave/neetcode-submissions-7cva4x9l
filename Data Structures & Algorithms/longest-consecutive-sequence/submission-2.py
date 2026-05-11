class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set: 
            # start of a sequence
            if num - 1 not in num_set:
                count = 1
                while num + 1 in num_set:
                    count += 1
                    num = num + 1
                res = max(res, count)
        return res


        