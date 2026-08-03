1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        if not node:
13            return None
14        old_new={}
15        old_new[node] = Node(node.val)
16        q = deque([node])
17        
18    
19        while q:
20            cur = q.popleft()
21            for nei in cur.neighbors:
22                if nei not in old_new:
23                    old_new[nei] = Node(nei.val)
24                    q.append(nei)
25
26                old_new[cur].neighbors.append(old_new[nei])
27
28        return old_new[node]