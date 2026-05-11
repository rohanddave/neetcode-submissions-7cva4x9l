class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        # row indices [0, m]
        # col indices [0, n]

        # i [0, m - 1]
        for i in range(self.m):
            for j in range(self.n): 
                r, c = i + 1, j + 1
                self.prefix[r][c] = matrix[r - 1][c - 1] + self.prefix[r][c - 1] + self.prefix[r - 1][c] - self.prefix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.prefix[r2][c2] - self.prefix[r2][c1 - 1] - self.prefix[r1 - 1][c2] + self.prefix[r1 - 1][c1 - 1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
'''
prefix sum 
row wise prefix sums = SC = O(n)
col wise prefix sum; SC = O(n)
SC: O(2 * n)

sumRegion((1, 1), (2, 2))
included cells = (1, 1), (1, 2), (2, 1), (2, 2)
prefix[1][1] = 3 + 0 + 5 + 6 
prefix[1][2] = 3 + 0 + 1 + 5 + 6 + 3 
prefix[2][1] = 3 + 0 + 5 + 6 + 1 + 2 
prefix[2][2] = 3 + 0 + 1 + 5 + 6 + 3 + 1 + 2 + 0
'''