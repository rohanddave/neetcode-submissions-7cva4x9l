# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bottom_up_dfs_postorder(p, q):
            if (p and not q) or (q and not p):
                return False 
            if not p and not q:
                return True
            
            l, r = bottom_up_dfs_postorder(p.left, q.left), bottom_up_dfs_postorder(p.right, q.right)
            return p.val == q.val and l and r
        return bottom_up_dfs_postorder(p, q)
        