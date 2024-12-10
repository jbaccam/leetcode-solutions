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
    public List<Integer> rightSideView(TreeNode root) {
        // if the tree is empty, return an empty list (example 4)
        if (root == null) {
            return new ArrayList<>();
        }

        // use queue for bfs
        Queue<TreeNode> queue = new LinkedList();
        queue.offer(root); // add root node to the queue
        List<Integer> result = new ArrayList<>();

        // traverse the tree level by level
        while (!queue.isEmpty()) {
            // get the number of nodes at the current level
            int size = queue.size();

            // process all the nodes on this level
            while (size-- > 0) {
                TreeNode current = queue.poll(); // remove the front node from the queue

                if (size == 0) { // if this is the last node at this level
                    result.add(current.val); // add the rightmost node of the level
                }

                if (current.left != null) { // add the left child to the queue
                    queue.offer(current.left);
                }

                if (current.right != null) { // add the right child to the queue
                    queue.offer(current.right);
                }
                
            }
        }
        return result;
    }
}