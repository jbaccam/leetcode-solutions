# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next # saving the next node because we are going to break the link

            # this line is what actually reverses the list
            curr.next = prev # save the previous value into the next (changing direction of the link)

            # these two lines are what iterates over the linked list
            prev = curr # now update prev to the curr, we updated the link but now we need to update the vals
            curr = temp # make curr go to the next node

        return prev # return prev cause thats the end, if we returned curr it would be ull
            