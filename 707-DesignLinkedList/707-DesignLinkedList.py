class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        # These are dummy nodes to deal with edge cases
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        cur = self.left.next
        # while curr is not null and we iterate index amt of times
        while cur and index > 0:
            cur = cur.next
            index -= 1
        # if curr is not null, not at the right dummy node, and the index is 0
        if cur and cur != self.right and index == 0:
            return cur.val
        # if it doesnt exist
        return -1



    def addAtHead(self, val: int) -> None:
        curNode, next, prev = ListNode(val), self.left.next, self.left
        prev.next = curNode
        curNode.prev = prev
        curNode.next = next
        next.prev = curNode
        

    def addAtTail(self, val: int) -> None:
        curNode, next, prev = ListNode(val), self.right, self.right.prev
        prev.next = curNode
        curNode.prev = prev
        curNode.next = next
        next.prev = curNode

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            curNode, next, prev = ListNode(val), cur, cur.prev
            prev.next = curNode
            curNode.prev = prev
            curNode.next = next
            next.prev = curNode
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)