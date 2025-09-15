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
        ListNode currentNode = head; // start at the head node
        ListNode prevNode = null; // prev of head is null (since we are reversing)

        while (currentNode != null) { // loop through all the nodes until we reach the end of the list
            ListNode nextNode = currentNode.next; // save this cause were gonna do some flip floppin and we dont wanna lose it

            // linked list have pointers that point to where the next and previous nodes are
            // so we have to change where the nodes point and their actual values
            // originally its like, 1 points to 2, 2 points to 3, 3 points to 4
            // since were going to be reversing, that means 1 will point to null, 2 will point to 1, 3 will point to 2

            currentNode.next = prevNode; // reverse (or flip) the pointer of the currentNode, to point to the previousNode  
            prevNode = currentNode; // move the prevNode pointer to the currentNode, so the nextNode will have an updated prevNode
            currentNode = nextNode; // this is almost like incrementing the node so next iteration the currentNode will be updated
        }
    return prevNode; // return prevNode because this will be the new head of the new list
    }
}
