# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: 
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False

        stack = [root]
        while stack: 
            curr = stack.pop()
            if self.helper(curr, subRoot):
                return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False
    def helper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: 
            return True
        if (not root and subRoot) or (root and not subRoot):
            return False
        stack1 = [root]
        stack2 = [subRoot]

        while stack1 and stack2: 
            curr1, curr2 = stack1.pop(), stack2.pop()
            # if curr not equal
            if curr1.val != curr2.val:
                return False
            # if left not equal
            if (curr1.left and curr2.left and curr1.left.val != curr2.left.val) or (curr1.left and not curr2.left) or (not curr1.left and curr2.left):
                return False
            # if right equal 
            if (curr1.right and curr2.right and curr1.right.val != curr2.right.val) or (curr1.right and not curr2.right) or (not curr1.right and curr2.right):
                return False
            
            if curr1.left:
                stack1.append(curr1.left)
            if curr1.right:
                stack1.append(curr1.right)
            if curr2.left:
                stack2.append(curr2.left)
            if curr2.right:
                stack2.append(curr2.right)
        
        if not stack1 and not stack2:
            return True
        return False

                


        