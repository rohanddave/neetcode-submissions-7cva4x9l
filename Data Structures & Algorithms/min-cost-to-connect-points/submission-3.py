import heapq 

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # select a start vertex 
        # explore all it's neighbors and pick the smallest cost one next
        # continue doing this till there is a heap and the length of visited < n
        n = len(points) 
        visited = set() 
        heap = [(0, (points[0][0], points[0][1]))]
        mst_cost = 0

        def compute_cost(p1, p2):
            print('compute cost called wit: ', p1, p2)
            x1, y1 = p1
            x2, y2 = p2 
            return abs(x1 - x2) + abs(y1 - y2)
    
        while heap and len(visited) < n: 
            cost, point = heapq.heappop(heap) 

            if point in visited:
                continue
            
            visited.add(point)
            mst_cost += cost

            for p in points: 
                nei_point = (p[0], p[1])
                if nei_point not in visited: 
                    nei_cost = compute_cost((p[0],p[1]), point)
                    print(nei_cost)
                    heapq.heappush(heap, (nei_cost,nei_point))
        return mst_cost


        