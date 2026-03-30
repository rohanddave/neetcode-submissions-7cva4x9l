class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = [] 

        def dfs(i, curr):
            if i >= len(nums):
                solutions.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            dfs(i + 1, curr)
        dfs(0, [])
        return solutions
            
        