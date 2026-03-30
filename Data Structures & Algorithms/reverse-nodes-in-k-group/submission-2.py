# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(curr, k): 
            k -= 1
            while curr and k > 0: 
                curr = curr.next
                k -= 1
            return curr 
        
        def reverse(head): 
            prev, curr = None, head
            while curr: 
                nex = curr.next
                curr.next = prev 
                prev = curr 
                curr = nex
            
            return (prev, head) # (head, tail)

        
        if not head:
            return None 
        
        curr = head
        res_head = head
        group_prev_tail = None
        while True: 
            kth = getKth(curr, k)
            if not kth:
                break
            
            # head and tail of current sublist of length k
            prev_head, prev_tail = curr, kth 

            # store the node after the end of this sublist since this will be start for next group
            new_start = prev_tail.next

            # make the next pointer of tail of current sublist none so that reverse function can stop 
            prev_tail.next = None 

            # reversing the current sublist returns the new head and tail of the sublist
            new_head, new_tail = reverse(prev_head)

            # if there is a sublist processed before the current one set it's tail.next = new_head of reveresed list
            if group_prev_tail: 
                group_prev_tail.next = new_head
            else:
                res_head = new_head
            
            # point the current tail to the new start in case the next group is < k length and hence the while loop breaks early
            new_tail.next = new_start
            
            # move the curr pointer to the start of the next sublist
            curr = new_start
            # update the prev group's tail to the recently processed group's tail
            group_prev_tail = new_tail

        
        return res_head
        