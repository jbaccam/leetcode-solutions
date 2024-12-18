/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        // base case
        if (root == null) {
            return null;
        }

        // if vlaue is greater than the roots value, go right
        if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else if (key < root.val) { // if its less than, go left
            root.left = deleteNode(root.left, key);
        } else { // node is found now to remove it
            if (root.left == null) { // no left child
                return root.right; // replace the node with its right child
            } else if (root.right == null) { // no right child
                return root.left; // replace the node with its left child
            } else { // it has both children
                TreeNode minNode = minValueNode(root.right); // find smallest value in the right subtree
                root.val = minNode.val; // replace the value of the current node with the smallest vlaue in the right subtree
                root.right = deleteNode(root.right, minNode.val); // remove it from the right subtree
            }
        }
        return root;
    }

    public TreeNode minValueNode(TreeNode root) {
        TreeNode current = root;
        // traverse left until the leftmost node is reached
        while (current != null && current.left != null) {
            current = current.left;
        }
        return current; // the leftmost node is the smallest node in the subtree
    }
}
