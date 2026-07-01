1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        graph=defaultdict(list)
4        def dfs(cur, target, visited):
5            if cur == target:
6                return True
7            visited.add(cur)
8            for nei in graph[cur]:
9                if nei not in visited:
10                    if dfs(nei, target, visited):
11                        return True
12            return False
13
14        for u, v in edges:
15            # 如果 u 已经能走到 v，再加 [u,v] 就形成环
16            if u in graph and v in graph:
17                if dfs(u, v, set()):
18                    return [u, v]
19
20            graph[u].append(v)
21            graph[v].append(u)
22
23        return []
24       
25        