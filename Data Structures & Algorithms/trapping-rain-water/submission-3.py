class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water = 0
        while l < r: 
            if height[l] < height[r]:
                l += 1
                l_max = max(l_max, height[l])
                water += (l_max - height[l]) 
                
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water += (r_max - height[r]) 
                
        return water


        