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
14        visited={}
15        def helper(node):
16            if node in visited:
17                return visited[node]
18            newnode=Node(node.val)
19            visited[node]=newnode
20            for nei in node.neighbors:
21                newnode.neighbors.append(helper(nei))
22            return newnode
23        return helper(node)
24                    