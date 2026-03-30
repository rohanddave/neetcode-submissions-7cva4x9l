# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        stack = [(root,0)]
        while stack:
            curr, index = stack.pop()
            # if new level
            if index > len(res) - 1:
                res.append([curr.val])
            else:
                res[index].append(curr.val)

            if curr.right:
                stack.append((curr.right, index + 1))
            if curr.left:
                stack.append((curr.left, index + 1))
            
        return res

        