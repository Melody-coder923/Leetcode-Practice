1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges)!=n-1:
4            return False
5        parents=parents = list(range(n))
6        def find(x):
7            if parents[x]!=x:
8                parents[x]=find(parents[x])
9            return parents[x]
10
11        def union(x,y):
12            root_x = find(x)
13            root_y=find(y)
14            if root_x==root_y:
15                return False
16            else:
17                parents[root_y]=root_x
18                return True
19            
20        
21        for u,v in edges:
22            if not union(u,v):
23                return False
24        return True