from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degrees = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degrees[course] += 1
        
        q = deque([])

        for i in range(len(in_degrees)):
            in_degree = in_degrees[i]
            if in_degree == 0: 
                q.append(i)

        visited = set() 
        while q:
            curr = q.popleft() 
            visited.add(curr)
            for neighbor in adj[curr]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0 and neighbor not in visited: 
                    visited.add(neighbor)
                    q.append(neighbor)
        return len(visited) == numCourses




        