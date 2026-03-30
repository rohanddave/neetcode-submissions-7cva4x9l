class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 

        for i, h in enumerate(heights):
            s = i
            while stack and stack[-1][1] > h:
                start, height = stack.pop()
                max_area = max(max_area, (i - start) * height)
                s = start
            stack.append((s, h))
        
        while stack: 
            start, height = stack.pop()
            max_area = max(max_area, (len(heights) - start) * height)

        return max_area
        