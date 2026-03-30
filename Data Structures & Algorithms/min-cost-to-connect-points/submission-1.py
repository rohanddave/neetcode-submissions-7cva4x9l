import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Prims: 
        pick one start point 
        add to heap 
        while heap and len(vistied) < len(points) 
        pop item 
        if node in visited skip 
        else add to mst 
        compute all not visited edges 

        '''
        def compute_cost(p1, p2): 
            x1, y1 = p1 
            x2, y2 = p2 
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(points)
        visited = set()
        heap = [(0, points[0])] 
        res = 0 

        while heap and len(visited) < n: 
            cost, point = heapq.heappop(heap)
            x, y = point
            if (x,y) in visited:
                continue 
            
            visited.add((x, y)) 
            res += cost 

            for nei in points: 
                if (nei[0], nei[1]) not in visited: 
                    heapq.heappush(heap, (compute_cost(nei, point), nei))
        return res       