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
15        q= deque([root])
16        while q:
17            size=len(q)
18            prev=None
19            for _ in range(size):
20                node=q.popleft()
21                if prev!=None:
22                    prev.next=node
23                prev=node              
24                if node.left:
25                    q.append(node.left)
26                if node.right:
27                    q.append(node.right)
28            prev.next=None
29
30        return root