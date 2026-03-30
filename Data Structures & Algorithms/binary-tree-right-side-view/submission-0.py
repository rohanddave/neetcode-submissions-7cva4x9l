# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        stack = [(root, 0)]
        levels = []
        while stack:
            curr, height = stack.pop()
            # new level
            if height > len(levels) - 1:
                levels.append([curr.val])
            else:
                levels[height].append(curr.val)

            if curr.left:
                stack.append((curr.left, height + 1))
            if curr.right:
                stack.append((curr.right, height + 1))
        res = []
        for i in range(0, len(levels)):
            res.append(levels[i][0])
        return res

            



        