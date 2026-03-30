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
        def dfs(node):
            if not node:
                res.append('null')
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root) 
        return ','.join(res)

    # preorder = [1,2,3,4,]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = collections.deque(data.split(','))

        def helper():
            val = q.popleft() 
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()


