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
        if not node:
            return node
        
        dict={} # old: new

        def helper(node):
            if node in dict:
                return dict[node]
            
            if not node:
                return None
            
            new_node=Node(node.val)
            dict[node]=new_node

            for nei in node.neighbors:
                new_node.neighbors.append(helper(nei))
            
            return new_node

        return helper(node)

