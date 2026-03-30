# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder_dfs(node):
            if not node:
                res.append("null")
                return 
            res.append(str(node.val))
            preorder_dfs(node.left)
            preorder_dfs(node.right)
        preorder_dfs(root)
        str_res = ','.join(res)
        return str_res
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(','))
        def dfs():
            val = next(vals)
            if val == "null":
                return None
            
            node = TreeNode(int(val), dfs(), dfs())
            return node
        return dfs()


# inorder (LNR) = [null,2,null,1,4,3,5]
# preorder (NLR) = [1,2,null,null,3,4,null,null,5,null,null]
# postorder (LRN) = []
