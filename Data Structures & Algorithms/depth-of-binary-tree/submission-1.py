# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bottom_up_dfs(node): 
            if not node:
                return 0
            
            left, right = bottom_up_dfs(node.left), bottom_up_dfs(node.right)

            return max(left, right) + 1
        return bottom_up_dfs(root)
        