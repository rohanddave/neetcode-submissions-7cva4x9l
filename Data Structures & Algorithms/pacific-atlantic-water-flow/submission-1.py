class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_set, atlantic_set = set(), set() 
        
        def dfs(r,c,reachable):
            reachable.add((r,c))

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < m and 0 <= new_c < n and (new_r,new_c) not in reachable and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r,new_c, reachable)
            
        for i in range(m):
            dfs(i, 0, pacific_set)
            dfs(i,n-1, atlantic_set)
        
        for j in range(n):
            dfs(0,j, pacific_set)
            dfs(m-1,j,atlantic_set)
        
        return list(atlantic_set & pacific_set)
        