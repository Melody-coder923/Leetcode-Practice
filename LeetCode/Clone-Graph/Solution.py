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
14        
15        visited = {}
16        
17        def dfs(n):
18            if n in visited:
19                return visited[n]
20            
21            copy = Node(n.val)
22            visited[n] = copy
23            
24            for nei in n.neighbors:
25                copy.neighbors.append(dfs(nei))
26            
27            return copy
28        
29        return dfs(node)