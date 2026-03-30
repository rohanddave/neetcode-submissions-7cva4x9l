from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q, adj = deque(), defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites: 
            adj[prereq].append(course) 
            in_degree[course] += 1
        
        visited = set() 

        for i in range(numCourses): 
            if in_degree[i] == 0: 
                q.append(i) 
                visited.add(i)
        
        res = [] 

        while q: 
            course = q.popleft() 
            res.append(course) 
            
            for nei in adj[course]: 
                if nei not in visited: 
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0: 
                        q.append(nei)
        return [] if len(res) < numCourses else res