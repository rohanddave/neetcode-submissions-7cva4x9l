# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        l, r = dummy, dummy.next
        i = 1
        while i <= n:
            r = r.next
            i+= 1
        while r:
            r = r.next
            l = l.next
        prev = l
        node = l.next
        nex = node.next if node else None
        prev.next = nex

        return dummy.next

        