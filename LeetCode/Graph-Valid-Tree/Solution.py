1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges)!=n-1:
4            return False
5        visited=set()
6        graph=defaultdict(list)
7        for u,v in edges:
8            graph[u].append(v)
9            graph[v].append(u)
10
11        def dfs(node,parent):
12            visited.add(node)
13            for nei in graph[node]:
14                if nei==parent:
15                    continue
16                if nei in visited:
17                    return False
18                if not dfs(nei,node):
19                    return False
20            
21            
22            return True
23        
24        if not dfs(0, -1):
25            return False
26        
27        return len(visited) == n