1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        graph=defaultdict(list)
4        for a,b in edges:
5            graph[a].append(b)
6            graph[b].append(a)
7        visited = [False]*n
8        count=0
9        
10        def dfs(node):
11            visited[node] = True
12            for neighbor in graph[node]:
13                if not visited[neighbor]:
14                    dfs(neighbor)
15                    
16        for i in range(n):
17            if visited[i]==False:
18                count+=1
19                dfs(i)
20        return count