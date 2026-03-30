# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # using postorder dfs
        def isSameTree(p, q):
            if (p and not q) or (q and not p):
                return False 
            if not p and not q:
                return True 
            
            l, r = isSameTree(p.left, q.left), isSameTree(p.right, q.right)
            return p.val == q.val and l and r
    
        q = deque([root])
        while q: 
            level_size = len(q)

            for _ in range(level_size): 
                curr = q.popleft() 
                if isSameTree(curr, subRoot):
                    return True 
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return False


        