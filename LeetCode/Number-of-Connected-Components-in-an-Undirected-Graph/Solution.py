1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        graph=defaultdict(list)
4        for u,v in edges:
5            graph[u].append(v)
6            graph[v].append(u)
7        
8        def dfs(node,visited):
9            visited.add(node)
10            for nei in graph[node]:
11                if nei not in visited:
12                    dfs(nei,visited)
13                
14        
15        visited=set()
16        count=0
17        for node in range(n):
18            if node not in visited:
19                dfs(node,visited)
20                count+=1
21        return count
22