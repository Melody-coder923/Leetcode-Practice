1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        if not head:
13            return None
14
15        node_map = {}
16        cur = head
17        while cur:
18            node_map[cur] = Node(cur.val)
19            cur = cur.next
20
21        cur=head
22        while cur:
23            if cur.next:
24                node_map[cur].next = node_map[cur.next]
25            if cur.random:
26                node_map[cur].random = node_map[cur.random]
27            cur = cur.next
28
29        return node_map[head]