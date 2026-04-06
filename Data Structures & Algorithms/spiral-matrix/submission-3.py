class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = [] 
        
        def helper(l, r, t, b):
            if l >= r or t >= b:
                return

            # move right 
            for j in range(l, r):
                res.append(matrix[t][j])
            t += 1

            if t >= b:
                return

            # move down 
            for i in range(t, b): 
                res.append(matrix[i][r - 1])
            r -= 1

            if l >= r:
                return

            # move left 
            for j in range(r - 1, l - 1, -1): 
                res.append(matrix[b - 1][j])
            b -= 1

            if t >= b:
                return

            # move up
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

            helper(l, r, t, b)
        helper(0, n, 0, m)
        return res
        