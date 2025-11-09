# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if not lists:
            return None
        
        # create dummy node to append onto
        dummy = ListNode(0)
        curr = dummy
        heap = []

        # put head of each list in our heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, i, node = heapq.heappop(heap)

            # add this node to our result 
            curr.next = node
            curr = curr.next


            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next

        
         