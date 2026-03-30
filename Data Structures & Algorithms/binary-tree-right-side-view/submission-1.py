# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return [] 
        
        q = deque([root])
        res = [] 
        while q: 
            level_size = len(q)
            
            for i in range(level_size): 
                curr = q.popleft() 
                if i == level_size - 1: 
                    res.append(curr.val)
                if curr.left: 
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res

        