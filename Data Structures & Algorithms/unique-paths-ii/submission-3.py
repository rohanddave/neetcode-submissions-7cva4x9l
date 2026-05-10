class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        robot starts top left 
        obstacle => 1
        space => 0 
        path to reach bottom right avoiding obstacles 
        find the number of possible unique paths from top left to bottom right avoiding obstacles
        '''
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        memo = {}
        def dfs(i, j): 
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            right = down = 0
            if (j + 1) < n and obstacleGrid[i][j + 1] != 1:
                right = dfs(i, j + 1)
            if (i + 1) < m and obstacleGrid[i + 1][j] != 1:
                down = dfs(i + 1, j)
            memo[(i, j)] = right + down 
            return memo[(i, j)]
        return dfs(0, 0)

        