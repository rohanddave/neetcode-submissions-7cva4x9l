class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        n = len(height)
        res = 0
        for r in range(n): 
            # maintain monotonic property 
            while stack and height[stack[-1]] < height[r]: 
                mid = stack.pop()

                if stack:
                    right = r
                    left = stack[-1]
                    bounded_height = min(height[right], height[left]) - height[mid]
                    curr = bounded_height * (right - left - 1)
                    res += curr
            
            stack.append(r)

        return res