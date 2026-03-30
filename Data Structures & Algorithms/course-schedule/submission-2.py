class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE, GREY, BLACK = 0,1,2
        color = [WHITE] * numCourses

        adj = collections.defaultdict(list)

        for course, pre in prerequisites:
            adj[pre].append(course)
        
        def hasCycle(course):
            color[course] = GREY

            for neighbor in adj[course]:
                if color[neighbor] == GREY:
                    return True 
                if color[neighbor] == WHITE:
                    if hasCycle(neighbor):
                        return True 
            color[course] = BLACK
            return False
        
        for i in range(numCourses):
            if color[i] == WHITE and hasCycle(i):
                return False 
        return True 


        