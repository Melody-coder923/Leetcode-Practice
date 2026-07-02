1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges)!=n-1:
4            return False
5        #如果有环就不是树
6        parents=list(range(n))
7        def find(x):
8            if parents[x]!=x:
9                parents[x]=find(parents[x])
10            return parents[x]
11        
12        def union(x,y):
13            root_x=find(x)
14            root_y=find(y)
15            if root_x==root_y:
16                return False
17            else:
18                parents[root_y]=root_x
19                return True
20        
21        for u,v in edges:
22            if not union(u,v):
23                return False
24        return True  