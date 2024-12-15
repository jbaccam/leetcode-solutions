class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null)
            return new TreeNode(val);
        insert(root, val);
        return root;
    }
    public static void insert(TreeNode root, int val) {
        if(root.val > val) {
            if(root.left == null)
                root.left = new TreeNode(val);
            else
                insert(root.left, val);
        }
        else if(root.val < val) {
            if(root.right == null)
                root.right = new TreeNode(val);
            else
                insert(root.right, val);
        }
    }
}