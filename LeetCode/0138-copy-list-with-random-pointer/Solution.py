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
        
        old_new = {None: None}
        cur=head
        while cur:
            newnode=Node(cur.val)
            old_new[cur]=newnode
            cur = cur.next
        
        cur=head
        while cur:
            new_node=old_new[cur]
            new_node.next=old_new[cur.next]
            new_node.random=old_new[cur.random]
            cur = cur.next
        
        return old_new[head]