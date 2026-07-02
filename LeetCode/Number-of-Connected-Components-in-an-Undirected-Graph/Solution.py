1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        graph=defaultdict(list)
4
5        for u,v in edges:
6            graph[u].append(v)
7            graph[v].append(u)
8        visited=set()
9        def dfs(node):
10            visited.add(node)
11            for nei in graph[node]:
12                if nei not in visited:
13                    dfs(nei)
14
15        
16        count=0
17        for node in range(n):
18            if node not in visited:
19                dfs(node)
20                count+=1
21        return count
22