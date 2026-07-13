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
14        graph={}
15        def build(node):
16            if node in graph:
17                return graph[node]
18            newNode=Node(node.val)
19            graph[node]=newNode
20            for nei in node.neighbors:
21                newNode.neighbors.append(build(nei))
22
23            return newNode
24
25        return build(node)
26