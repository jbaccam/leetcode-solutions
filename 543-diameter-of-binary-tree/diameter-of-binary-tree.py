# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr: # null node
                return 0

            # otherwise lets do the recursive case
            # get the height of the left subtree
            left = dfs(curr.left)

            # height of right subtree
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right) # gotta return +1 so we actaully get the height

        # call our recursive function
        dfs(root)
        
        # return the val
        return self.res