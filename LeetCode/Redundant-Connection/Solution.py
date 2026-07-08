1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]: 
3        graph=defaultdict(list)
4        def dfs(node,target,visited):
5            if node==target:
6                return True
7            visited.add(node)
8            for nei in graph[node]:
9                if nei not in visited:
10                    if dfs(nei,target,visited):
11                        return True
12            return False
13
14        
15
16        for u,v in edges:
17            if u in graph and v in graph:
18                if dfs(u,v,set()):
19                    return [u,v]
20            graph[u].append(v)
21            graph[v].append(u)
22        return []
23
24
25