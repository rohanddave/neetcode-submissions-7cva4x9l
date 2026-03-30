class Solution:
    def numDecodings(self, s: str) -> int:
        self.count, n = 0, len(s)
        res = []

        def dfs(i): 
            if i >= n: 
                self.count += 1
                return 
            if s[i] == '0':
                return

            dfs(i + 1)
            if (i + 1) < n and 10 <= int(s[i: i + 2]) <= 26:
                dfs(i + 2)
        dfs(0)
        return self.count
        