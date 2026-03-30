# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Approach 1: 
        reverse both lists 
        9 <- 9; 8 <- 9 <- 7
        while l1 and l2: summ = l1.val + l2.val + carry (27; 27 % 10 = 7; carry = 27 // 10)

        x -> 6 -> 9 -> 
        '''
        def reverse(l):
            prev = None 
            while l: 
                nex = l.next
                l.next = prev
                prev = l
                l = nex
            return prev

        # reverse lists 
        prev1, prev2 = reverse(l1), reverse(l2)
        
        dummy = ListNode()
        curr = dummy
        carry = 0
        while prev1 and prev2: 
            summ = prev1.val + prev2.val + carry 
            digit = summ % 10 
            carry = summ // 10

            curr.next = ListNode(digit)
            curr = curr.next

            prev1 = prev1.next
            prev2 = prev2.next
        
        while prev1: 
            summ = prev1.val + carry 
            digit = summ % 10 
            carry = summ // 10

            curr.next = ListNode(digit)
            curr = curr.next
            prev1 = prev1.next
        
        while prev2: 
            summ = prev2.val + carry 
            digit = summ % 10 
            carry = summ // 10

            curr.next = ListNode(digit)
            curr = curr.next
            prev2 = prev2.next
        
        if carry: 
            curr.next = ListNode(carry)
            curr = curr.next
        
        
        return reverse(dummy.next)


        
            


        