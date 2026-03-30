# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def bottom_up_postorder_dfs(node): 
            if not node: 
                return 0
            
            left = bottom_up_postorder_dfs(node.left)
            right = bottom_up_postorder_dfs(node.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1
        bottom_up_postorder_dfs(root)
        return self.diameter
            

        