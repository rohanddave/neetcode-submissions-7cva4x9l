class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic_set, pacific_set = set(), set() 
        r, c = len(heights), len(heights[0])

        def dfs(i, j, reachable):
            if (i, j) in reachable:
                return 
            
            reachable.add((i, j))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < r and 0 <= new_j < c and heights[i][j] <= heights[new_i][new_j]:
                    dfs(new_i, new_j, reachable)


        # left and right edges
        for i in range(r):
            dfs(i, 0, pacific_set)
            dfs(i, c - 1, atlantic_set)
        
        # top and bottom edges 
        for j in range(c): 
            dfs(0, j, pacific_set)
            dfs(r - 1, j, atlantic_set)     


        return list(atlantic_set & pacific_set)
        