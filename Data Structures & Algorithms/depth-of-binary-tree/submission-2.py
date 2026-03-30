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
        
        def top_down_dfs(node, depth): 
            if not node:
                return depth 
            
            left, right = top_down_dfs(node.left, depth + 1), top_down_dfs(node.right, depth + 1)
            return max(left, right)
            


        # return bottom_up_dfs(root)
        return top_down_dfs(root, 0)
        