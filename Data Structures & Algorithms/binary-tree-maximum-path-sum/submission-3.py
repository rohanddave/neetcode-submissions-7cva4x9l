# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # bottom up dfs (prolly need to pass state since the path is not necessary to exist through the root or track globlaly? )
        self.res = float('-inf')
        def dfs(node):
            if not node:
                return float('-inf') 
            
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))

            self.res = max(self.res, l + r + node.val)
            return max(l, r) + node.val
        dfs(root)
        return self.res
            