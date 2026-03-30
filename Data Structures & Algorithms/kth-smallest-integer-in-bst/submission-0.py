import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        heap = []
        res = -1
        while stack:
            curr = stack.pop()
            heapq.heappush(heap, curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        for i in range(0, k):
            res = heapq.heappop(heap)
        return res
        
        