# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # so we can do a bfs, where we always take the right most element of the layer
        # we know that bfs is implemented with a queue, so when all the elements of a layer is added to the queue
        # BEFORE we pop to move to the next layer, what we can do is we can take the last element of the queue
        # and add that to our result, because that will be the right most element in the layer
        res = []
        queue = deque([root])

        while queue:
            rightSide = None # initially set as null
            queue_len = len(queue)

            # go over every node in this level
            for i in range(queue_len):
                cur = queue.popleft()
                if cur: # node could be null
                    rightSide = cur # rightSide will get continously updated until we reach the last element of queue, which it will then become
                    # the right most element
                    queue.append(cur.left) # always add left before right so its in order
                    queue.append(cur.right)
            if rightSide: # right side could be null 
                res.append(rightSide.val)
        
        return res
