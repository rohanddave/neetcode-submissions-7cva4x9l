# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, 0)[0]
    def helper(self, root: Optional[TreeNode], height: int) -> (bool, int):
        if not root:
            return (True, height)
        
        l_balanced, l_height = self.helper(root.left, height + 1)
        r_balanced, r_height = self.helper(root.right, height + 1)

        return (l_balanced and r_balanced and abs(l_height - r_height) <= 1, max(l_height, r_height))