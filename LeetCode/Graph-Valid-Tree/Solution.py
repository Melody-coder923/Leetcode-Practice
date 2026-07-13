1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges)!=n-1:
4            return False
5        graph=defaultdict(list)
6        for u,v in edges:
7            graph[u].append(v)
8            graph[v].append(u)
9        #如果有环就不是树
10        visited=set()
11        def dfs(node, parent):
12            visited.add(node)
13            for nei in graph[node]:
14                if nei == parent:
15                    continue
16                if nei in visited:
17                    return False
18                if not dfs(nei, node):
19                    return False
20            return True
21
22        if not dfs(0, -1):
23            return False
24        return len(visited) == n
25
26
27       