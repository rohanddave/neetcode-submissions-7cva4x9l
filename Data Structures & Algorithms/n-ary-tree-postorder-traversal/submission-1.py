"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # postorder = LRN
        self.res = [] 
        def dfs(node):
            if not node:
                return 
            
            for child in node.children: 
                dfs(child)
            self.res.append(node.val)
        dfs(root)
        return self.res
        