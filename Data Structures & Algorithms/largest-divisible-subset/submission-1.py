import sys
sys.setrecursionlimit(2000)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        def dfs(i, j): 
            if i == len(nums):
                return []
            if (i, j) in memo:
                return memo[(i, j)]
            
            pick = []
            if j == -1 or nums[i] % nums[j] == 0:
                pick = [nums[i]] + dfs(i + 1, i)
            skip = dfs(i + 1, j)

            memo[(i, j)] = pick if len(pick) > len(skip) else skip
            return memo[(i, j)]
        return dfs(0, -1)
        