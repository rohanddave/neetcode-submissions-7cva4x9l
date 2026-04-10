# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder= NLR; inorder= LNR
        m = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0
        
        def dfs(l, r): 
            # some base case here 
            if l > r: 
                return None 
            
            root = TreeNode(preorder[self.preorder_idx])
            self.preorder_idx += 1
            root.left = dfs(l, m[root.val] - 1)
            root.right = dfs(m[root.val] + 1, r)
            return root
        return dfs(0, len(preorder) - 1)

