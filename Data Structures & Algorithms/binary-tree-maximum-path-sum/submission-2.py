# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def helper(node): 
            if not node: 
                return 0 
            
            l = max(0, helper(node.left))
            r = max(0, helper(node.right))
        
            self.res = max(self.res, node.val + l + r)
            return node.val + max(l, r)
        helper(root)
        return self.res
            

        