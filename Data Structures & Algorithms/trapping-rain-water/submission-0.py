class Solution:
    def trap(self, height: List[int]) -> int:
        # height =       [0,2,0,3,1,0,1,3,2,1]
        # next greater = [2,3,3,3,1,1,3,-1,-1,-1]
        # prev greater = [-1,-1,2,-1,3,3,1,-1,3,2]
        n = len(height)
        next_greater = [-1] * n
        prev_greater = [-1] * n

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= height[i]:
                stack.pop()
            if stack:
                next_greater[i] = max(stack)
            stack.append(height[i])
        stack = []
        for i in range(n):
            while stack and stack[-1] <= height[i]:
                stack.pop()
            if stack:
                prev_greater[i] = max(stack)
            stack.append(height[i])
        print(next_greater)
        print(prev_greater)
        res = 0
        for i in range(n):
            if next_greater[i] != -1 and prev_greater[i] != -1:
                curr = min(next_greater[i], prev_greater[i]) - height[i]
                res += curr
                print(i, next_greater[i], prev_greater[i], curr)

        return res
             
        