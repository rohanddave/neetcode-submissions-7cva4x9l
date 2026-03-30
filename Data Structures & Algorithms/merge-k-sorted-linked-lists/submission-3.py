# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] 

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode()
        curr = dummy 

        while heap: 
            curr_val, list_index, curr_node = heapq.heappop(heap)
            curr.next = curr_node
            curr = curr.next
            # res.append(curr_node)
            if curr_node.next: 
                heapq.heappush(heap, (curr_node.next.val, list_index, curr_node.next))
        return dummy.next    