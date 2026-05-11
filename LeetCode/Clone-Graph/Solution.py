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
14        visited = {}
15
16        def dfs(node):
17            if node in visited:
18                return visited[node]
19            
20            newNode=Node(node.val)
21            visited[node]=newNode
22
23            for nei in node.neighbors:
24                newNode.neighbors.append(dfs(nei))
25            return newNode
26        return dfs(node)