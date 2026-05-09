class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
        we want to return the largest subset of strs with at most m 0's and n 1's
        decision at each element is to pick or not pick into subset 
        we pre compute the number of 0's and 1's in each element and store in hashmap 
        when making decision: 
        pick = dfs(i + 1, zeros - number of zeros in strs[i], ones - number of ones in strs[i])
        skip = dfs(i + 1, zeros, ones) 
        dfs functions returns the largest number of strs 
        if zeros == 0 and ones == 0: return 0 
        else return max(skip, 1 + pick)
        '''

        counts = {} 
        for i, s in enumerate(strs): 
            zeros = 0
            for char in s: 
                if char == '0':
                    zeros += 1
            counts[i] = (zeros, len(s) - zeros)
        
        memo = {}
        def dfs(i, zeros, ones): 
            if zeros == 0 and ones == 0:
                return 0 
            if i == len(strs):
                return 0
            if (i, zeros, ones) in memo:
                return memo[(i, zeros, ones)]
            
            pick = 0
            if zeros - counts[i][0] >= 0 and ones - counts[i][1] >= 0:
                pick = 1 + dfs(i + 1, zeros - counts[i][0], ones - counts[i][1])
            skip = dfs(i + 1, zeros, ones)
            memo[(i, zeros, ones)] = max(skip, pick)
            return memo[(i, zeros, ones)]
        return dfs(0, m, n)
        