import heapq 

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)] 
        visited = set()

        while heap: 
            cost, r, c = heapq.heappop(heap)

            if r == (n - 1) and c == (n - 1):
                return cost 
            
            visited.add((r, c))

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(cost, grid[nr][nc]), nr, nc))
        return -1
                    

        