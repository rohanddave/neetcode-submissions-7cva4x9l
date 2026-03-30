# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bottom_up_recursive_postorder_dfs(node): 
            if not node: 
                return 
            
            bottom_up_recursive_postorder_dfs(node.left)
            bottom_up_recursive_postorder_dfs(node.right)

            tmp = node.left
            node.left = node.right 
            node.right = tmp 
            return
        
        def bottom_up_recursive_preorder_dfs(node):
            if not node:
                return 
            
            tmp = node.left 
            node.left = node.right 
            node.right = tmp 

            bottom_up_recursive_preorder_dfs(node.right)
            bottom_up_recursive_preorder_dfs(node.left)

        bottom_up_recursive_preorder_dfs(root)

        return root

        