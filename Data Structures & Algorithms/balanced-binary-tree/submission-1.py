# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def bottom_up_postorder_dfs(node): 
            if not node: 
                return (True, 0)
            
            l_balanced, l_height = bottom_up_postorder_dfs(node.left)
            r_balanced, r_height = bottom_up_postorder_dfs(node.right)

            curr_balanced = l_balanced and r_balanced and (abs(l_height - r_height) <= 1)
            return (curr_balanced, max(l_height, r_height) + 1)
        return bottom_up_postorder_dfs(root)[0]
            

            


        