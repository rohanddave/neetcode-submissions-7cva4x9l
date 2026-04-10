# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        self.post_idx = n - 1
        m = {val: idx for idx, val in enumerate(inorder)}
        # inorder = LNR; postorder = LRN

        # inorder from [l, r]
        def dfs(l, r): 
            if l > r: 
                return None 
            
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            mid = m[root_val]
            root.right = dfs(mid + 1, r)
            root.left = dfs(l, mid - 1)
            return root
        return dfs(0, n - 1)

            

