# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        stack1, stack2 = [p], [q]
        while stack1 and stack2:
            curr1, curr2 = stack1.pop(), stack2.pop()
            # curr node should be the same
            if (not curr1 and not curr2) or ((curr1 and curr2) and (curr1.val == curr2.val)):
                # left subtree should be the same
                if ((curr1.left and curr2.left) and (curr1.left.val == curr2.left.val)) or (not curr1.left and not curr2.left):
                    if curr1.left:
                        stack1.append(curr1.left)
                    if curr2.left:
                        stack2.append(curr2.left)
                else:
                    return False
                
                # right subtree should be the same
                if ((curr1.right and curr2.right) and (curr1.right.val == curr2.right.val)) or (not curr1.right and not curr2.right):
                    if curr1.right:
                        stack1.append(curr1.right)
                    if curr2.right:
                        stack2.append(curr2.right)
                else:
                    return False
            else:
                return False
        
        if (stack1 and not stack2) or (stack2 and not stack1):
            return False
        
        return True
        