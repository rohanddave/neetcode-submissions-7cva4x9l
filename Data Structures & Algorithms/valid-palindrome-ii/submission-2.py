class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(i, j, k): 
            l, r = i, j
            while l <= r: 
                if s[l] == s[r]: 
                    l += 1
                    r -= 1
                elif k > 0: 
                    return helper(l + 1, r, 0) or helper(l, r - 1, 0)
                else: 
                    return False 
            return True 

        return helper(0, len(s) - 1, 1)

        