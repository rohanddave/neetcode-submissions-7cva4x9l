# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2:
            addition = carry
            if l1: 
                addition = addition + l1.val
                l1 = l1.next
            if l2:
                addition = addition + l2.val
                l2 = l2.next
            res = addition % 10
            carry = addition // 10
            curr.next = ListNode(res)
            curr = curr.next
        
        # if there is still a carry
        if carry != 0: 
            curr.next = ListNode(carry)

        return dummy.next

        