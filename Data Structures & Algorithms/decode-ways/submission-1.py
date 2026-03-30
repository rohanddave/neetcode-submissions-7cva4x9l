class Solution:
    def numDecodings(self, s: str) -> int:
        mapping = {} 
        for i in range(ord('A'), ord('Z') + 1):
            mapping[i - ord('A') + 1] = chr(i)
        print(mapping)
        def dfs(i): 
            if i >= len(s): 
                return 1
            if s[i] == "0":
                return 0
            
            count = dfs(i + 1)
            if i + 1 < len(s) and int(s[i: i + 2]) in mapping: 
                count += dfs(i + 2)
            return count 
        return dfs(0)
            

        