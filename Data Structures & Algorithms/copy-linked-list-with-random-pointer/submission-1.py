"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy = {} 

        def dfs(node): 
            if not node:
                return None 
            if node in copy: 
                return copy[node]
            
            copy_node = Node(node.val)
            copy[node] = copy_node
            copy_node.next = dfs(node.next)
            copy_node.random = dfs(node.random)
            return copy_node
        
        dfs(head)
        return copy[head]
            

        
        