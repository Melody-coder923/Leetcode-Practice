1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        n=len(edges)
4        parents=list(range(n+1))
5
6        def find(x):
7            if parents[x]!=x:
8                parents[x]=find(parents[x])
9            return parents[x]
10        def union(x,y):
11            root_x=find(x)
12            root_y=find(y)
13            if root_x!=root_y:
14                parents[root_y]=root_x
15                return True     
16            return False
17        
18
19        for u,v in edges:
20            if not union(u,v):
21                return [u, v]
22        
23