"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clones = {}
        visited = set() 

        def dfs(node): 
            if not node:
                return 
            
            clone = Node(node.val)
            clones[node.val] = clone

            for neighbor in node.neighbors: 
                if neighbor.val not in clones: 
                    clone.neighbors.append(dfs(neighbor))
                else:
                    clone.neighbors.append(clones[neighbor.val])
            
            return clone
        
        return dfs(node)

        