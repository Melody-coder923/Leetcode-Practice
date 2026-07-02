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
14        graph=defaultdict(Node)
15      
16        def dfs(node):
17            if node in graph:
18                return graph[node]
19            newNode=Node(node.val)
20            graph[node]=newNode
21            for nei in node.neighbors:
22                newNode.neighbors.append(dfs(nei))
23            return newNode
24        
25        return dfs(node)
26        