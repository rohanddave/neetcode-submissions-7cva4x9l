# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # preorder = NLR
        # preorder1 = [1,3,5,null,null,null,2,null,null]
        # preorder2 = [2,1,null,4,null,null,3,null,7,null,null]
        # newpreorder = [3,4,5,4,null,null,5,null,7,null,null]
        def dfs(n1, n2):
            if not n1 and not n2:
                return None 
            if n1 and not n2:
                return n1 
            if n2 and not n1:
                return n2 
            
            node = TreeNode(n1.val + n2.val, dfs(n1.left,n2.left), dfs(n1.right,n2.right))
            return node
        return dfs(root1, root2)
        # BFS approach 
        # q1, q2 = deque([(root1, 0)]), deque([(root2, 0)])
        # while q1 and q2: 
        #     level_size = 2 ** q1[0][1]
        #     level = []

        #     for _ in range(level_size): 
        #         curr1, curr2 = q1.popleft()[0], q2.popleft()[0]
        #         if curr1.left or curr2.left:
        #             q1.append(curr1.left if curr1.left else)
            

        