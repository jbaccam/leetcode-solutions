# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 # for addition when we have to carry a number
        dummy = ListNode() # this is how we are going to start our new list, with a dummy node
        cur = dummy

        while l1 or l2 or carry:
            # one of the values could be null, so lets get the digits from them
            # so get the digits from l1 if its not null, if its null then its 0 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # compute the new digit
            val = v1 + v2 + carry
            # could potentially have a new carry
            carry = val // 10 # we only want the carry val, so for example if 
            # v1 + v2 + carry was 9 + 3 + 1, and we got 10, we have another carry of 1
            # for val we only want the ones place
            val = val % 10
            
            # now insert the new val
            cur.next = ListNode(val)
            # update our pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next