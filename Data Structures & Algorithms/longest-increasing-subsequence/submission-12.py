import sys
sys.setrecursionlimit(2000)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        length of longest strictly increasing subsequence 

        dfs function returns the length of longest strictly increasing subsequence 
        starting from index i 
        '''
        memo = {}

        def dfs(i, j): 
            if i == len(nums):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            pick = 0
            if j == -1 or nums[i] > nums[j]:
                pick = 1 + dfs(i + 1, i)
            skip = dfs(i + 1, j)
            memo[(i, j)] = max(pick, skip)
            return memo[(i, j)]
        return dfs(0, -1)

            

            
        