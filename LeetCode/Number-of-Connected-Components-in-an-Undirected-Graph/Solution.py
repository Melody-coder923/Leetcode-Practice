1from typing import List
2from collections import defaultdict
3
4class Solution:
5    def countComponents(self, n: int, edges: List[List[int]]) -> int:
6        # Step 1: 建图
7        graph = defaultdict(list)
8        for a, b in edges:
9            graph[a].append(b)
10            graph[b].append(a)  # 无向图：双向边
11
12        visited = set()
13        count = 0
14
15        # Step 2: 对每个节点尝试 DFS
16        def dfs(node):
17            if node in visited:
18                return
19            visited.add(node)
20            for neighbor in graph[node]:
21                dfs(neighbor)
22
23        for i in range(n):
24            if i not in visited:
25                dfs(i)
26                count += 1  # 每次新的 DFS 表示一个连通分量
27
28        return count
29