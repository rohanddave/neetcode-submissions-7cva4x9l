# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        count = 0
        while stack:
            curr, greatest = stack.pop()
            if curr.val >= greatest:
                count += 1
            if curr.left:
                stack.append((curr.left, max(greatest, curr.left.val)))
            if curr.right:
                stack.append((curr.right, max(greatest, curr.right.val)))
        return count
        