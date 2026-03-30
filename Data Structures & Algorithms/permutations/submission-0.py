class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        solutions = []

        def helper(options, curr):
            if len(curr) == len(nums):
                solutions.append(curr.copy())
                return
            
            for option in options:
                new_options = options.copy()
                new_options.remove(option)
                curr.append(option)
                helper(new_options, curr)
                curr.pop()
        helper(nums, [])
        return solutions

        