# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # so what we can do here, is we can recurisevly go through each node in the root tree, and we can pass in the root 
        # or child of that root and check if that sub tree is the same as the subroot, if it is, return true
        # if its not the same, check the other nodes in the root tree

        # an empty tree (subRoot is None) is always considered a subtree of any tree
        # also a base case cause recursion stops here for an empty subRoot
        if not subRoot:
            return True
        
        # main tree is empty but subRoot is not, 
        # recursion stops here if the main tree has no nodes left to check
        if not root:
            return False
        
        # check if these roots lead the same tree
        if self.isSameTree(root, subRoot):
            return True
        # if it didnt return True then check other nodes
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # helper function to check if its the same tree
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case, reached the bottom of a tree 
        if not root and not subRoot:
            return True
        
        # if the values are both existing, and the same, check and see if their children are the same also
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        
        # if we reached here its because the vals werent the same or because 
        return False
        
            
