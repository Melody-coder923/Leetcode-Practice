"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        old_new={}
        def build(node):
            if not node:
                return None
                
            if node in old_new:
                return old_new[node]

            new_node=Node(node.val)
            old_new[node]=new_node

            new_node.next=build(node.next)
            new_node.random=build(node.random)

            return new_node

        
        return build(head)
            