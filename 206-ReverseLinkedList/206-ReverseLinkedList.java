/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prevNode = null; // initialize previous pointer to null
        ListNode currentNode = head; // head will be the current position

        while (currentNode != null) { // loop until we go through all the nodes
            ListNode nextNode = currentNode.next; // create a next listNode and save it before we break the link

            currentNode.next = prevNode; // reverse the pointer by setting the next to prev

            // we can think of the two lines above as almost flipping the arrow
            prevNode = currentNode; // now set prev forward to the currnet node

            currentNode = nextNode; // increment and move the current forward to the next node
        }

        return prevNode;

    }
}