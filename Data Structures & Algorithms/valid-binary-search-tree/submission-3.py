# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack: 
            curr, lowerBound, upperBound = stack.pop()
            if curr.val <= lowerBound or curr.val >= upperBound:
                return False
            if curr.left:
                stack.append((curr.left, lowerBound, min(upperBound, curr.val)))
            if curr.right:
                stack.append((curr.right, max(lowerBound, curr.val),upperBound))
        return True

        