# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack: 
            node = stack.pop()
            if self.isSameTree(node, subRoot):
                return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False 
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)