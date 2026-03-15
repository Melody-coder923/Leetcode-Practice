1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10
11class Solution:
12    def connect(self, root: 'Node') -> 'Node':
13        if not root:
14            return root
15        queue=collections.deque([root])
16    
17        while queue:
18            level_size=len(queue)
19            prev=None
20            for _ in range(level_size):
21                node=queue.popleft()
22                if prev:
23                    prev.next=node
24                prev=node
25                if node.left:
26                    queue.append(node.left)
27                if node.right:
28                    queue.append(node.right)
29        return root
30