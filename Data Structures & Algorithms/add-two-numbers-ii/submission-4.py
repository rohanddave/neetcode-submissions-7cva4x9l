# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Approach 2: 

        traverse each list and add values to stack: 
        stack1 = [1,2,3]
        stack2 = [4,5,6]

        while stack1 and stack2: 
            pop element from each 
            calculate summ 
            calculate digit and carry 
            create listnode as curr and reverse 
        '''
        def reverse(l):
            prev = None
            while l: 
                nex = l.next
                l.next = prev
                prev = l 
                l = nex
            return prev
        s1, s2 = [], []
        curr1, curr2 = l1, l2
        while curr1 or curr2: 
            if curr1:
                s1.append(curr1.val)
                curr1 = curr1.next
            
            if curr2:
                s2.append(curr2.val)
                curr2 = curr2.next
        carry = 0
        dummy = ListNode()
        curr = dummy
        while s1 or s2:
            a, b =  s1.pop() if s1 else 0, s2.pop() if s2 else 0

            summ = a + b + carry
            digit = summ % 10 
            carry = summ // 10

            curr.next = ListNode(digit)
            curr = curr.next
        
        if carry: 
            curr.next = ListNode(carry)

        return reverse(dummy.next)



        
            


        