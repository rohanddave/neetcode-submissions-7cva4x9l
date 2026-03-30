class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(current, o, c):
            if o == 0 and c == 0:
                res.append(''.join(current))
                return 
            
            if o > 0:
                current.append("(")
                dfs(current, o - 1, c)
                current.pop()
            
            if c > o:
                current.append(")")
                dfs(current, o, c - 1)
                current.pop()
        dfs([], n, n)
        return res
        