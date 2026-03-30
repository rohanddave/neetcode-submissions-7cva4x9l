# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        
        prev, curr = None, slow 
        while curr: 
            new_curr = curr.next
            curr.next = prev 
            prev = curr 
            curr = new_curr
        
        n1, n2 = head, prev
        while n2 and n2.next: 
            new_n1, new_n2 = n1.next, n2.next

            n1.next = n2 
            n2.next = new_n1 

            n1 = new_n1 
            n2 = new_n2
        
        