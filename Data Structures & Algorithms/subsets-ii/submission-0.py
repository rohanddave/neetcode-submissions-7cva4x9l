class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        def dfs(i, curr):
            if i >= len(nums):
                solutions.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr)
            item_popped = curr.pop()
            while i < len(nums) and nums[i] == item_popped:
                i += 1
            dfs(i, curr)
        dfs(0, [])
        return solutions
        