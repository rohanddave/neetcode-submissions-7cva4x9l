class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.m = {'2': ['a','b','c'], '3': ['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9': ['w','x','y','z']}
        self.res = []

        def dfs(start, current):
            if start >= len(digits):
                self.res.append(''.join(current))
                return 

            for alpha in self.m[digits[start]]: 
                current.append(alpha)
                dfs(start + 1, current)
                current.pop()

        dfs(0, [])
        return self.res
        