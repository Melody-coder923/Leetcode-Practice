1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if n-1!=len(edges):
4            return False
5        
6        dic=defaultdict(list)
7        for u,v in edges:
8            dic[u].append(v)
9            dic[v].append(u)
10
11        visited=set()
12        def dfs(node,parent):
13            visited.add(node)
14            for nei in dic[node]:
15                if nei==parent:
16                    continue
17                if nei in visited:
18                    return False
19                if not dfs(nei,node):
20                    return False
21            return True
22
23        if not dfs(0, -1):
24            return False
25
26        return len(visited) == n
27
28
29
30     