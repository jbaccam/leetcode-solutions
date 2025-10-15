"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # this will track if we created a copy of the node we are checking already
        oldToNew = {}

        def dfs(node):
            # already made a clone, return the clone (new node)
            if node in oldToNew:
                return oldToNew[node]
                
            # clone doesnt exit so create it
            copy = Node(node.val)
            # add it to hashmap
            oldToNew[node] = copy

            # dfs the neighbors to make copies of every single neighbor
            for n in node.neighbors:
                copy.neighbors.append(dfs(n)) 
            # once were done making all the copies of the neighbors return the copy we just made
            return copy
        
        return dfs(node) if node else None
