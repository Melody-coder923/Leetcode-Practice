1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges)!=n-1:
4            return False
5
6        graph=defaultdict(list)
7        for u,v in edges:
8            graph[u].append(v)
9            graph[v].append(u)
10
11        visited=set()
12        def dfs(node,parent):
13            if node in visited:
14                return False
15            visited.add(node)
16            for nei in graph[node]:
17                if nei==parent:
18                    continue 
19                if not dfs(nei, node):
20                    return False
21            return True
22            
23        if not dfs(0,-1):
24            return False        
25
26        return len(visited)==n