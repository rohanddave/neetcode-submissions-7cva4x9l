class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def helper(i, j): 
            count = 0
            while i >= 0 and j < n and s[i] == s[j]: 
                count += 1
                i -= 1
                j += 1
            print(s[i + 1: j], i, j)
            return count
        res = 0
        for i in range(n):
            even, odd = helper(i, i + 1), helper(i, i)
            print(even, odd)
            res += even + odd 
        return res
            

        