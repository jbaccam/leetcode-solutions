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
    public TreeNode searchBST(TreeNode root, int val) {
        // base case
        if(root == null){
            return null;
        }

        // if val is greater than, then we search to the right
        if (val > root.val) {
            return searchBST(root.right, val);
        // if val is less than, we search to the left
        } else if (val < root.val) {
            return searchBST(root.left, val);
        } else {
            // if we found then return it !
            return root;
        }
    }
}