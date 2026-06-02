1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        parent=[i for i in range(len(edges)+1)]
4
5        def find(x):
6            if parent[x] != x:
7                parent[x]=find(parent[x])
8            return parent[x]
9
10        def union(u,v):
11            root_u=find(u)
12            root_v=find(v)
13            if root_u==root_v:
14                return False
15            parent[root_v]=root_u
16            return True
17        for u,v in edges:
18            if not union(u,v):
19                return [u,v]