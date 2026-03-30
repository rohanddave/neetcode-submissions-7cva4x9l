class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 

        def dfs(start, current):
            def is_palindrome(seg):
                return seg == seg[::-1]

            if start == len(s):
                res.append(current[:])
                return 
            
            for end in range(start + 1, len(s) + 1):
                segment = s[start:end]
                if is_palindrome(segment):
                    current.append(segment)
                    dfs(end, current)
                    current.pop()
        dfs(0, [])
        return res

        