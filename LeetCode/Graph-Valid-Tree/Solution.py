1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        #tree: 1. no loop  2.edges=n-1 3. no independant node
4        if len(edges) != n-1:
5            return False
6        graph=defaultdict(list)
7        for u,v in edges:
8            graph[u].append(v)
9            graph[v].append(u)
10        visited=set()
11        def dfs(node,parent):
12            if node in visited:
13                return False
14            visited.add(node)
15            for nei in graph[node]:
16                if nei==parent:
17                    continue 
18                if not dfs(nei, node):
19                    return False
20            return True
21        
22        if not dfs(0,-1):
23            return False
24        return len(visited)==n
25
26        
27
28