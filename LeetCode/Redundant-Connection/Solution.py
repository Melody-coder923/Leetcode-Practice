1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        # tree: n nodes and n-1=edges
4        # no indepent node
5        # connect but without cycle 
6
7        n=len(edges)
8        parents = list(range(n + 1))
9
10        def find(x):
11            if parents[x] != x:
12                parents[x] = find(parents[x])  
13            return parents[x]
14        
15        def union(x,y):
16            root_x= find(x)
17            root_y= find(y)
18            if root_x==root_y:
19                return False
20            parents[root_y]=root_x
21            return True
22        
23        res=[]
24        for u,v in edges:
25            if not union(u,v):
26                return [u,v]
27    