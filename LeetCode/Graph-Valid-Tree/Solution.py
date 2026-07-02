1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges)!=n-1:
4            return False
5        parent=[i for i in range(n)]
6        rank=[0]*n
7        def find(x):
8            if parent[x]!=x:
9                parent[x]=find(parent[x])
10            return parent[x]
11        
12        def union(x,y):
13            root_x= find(x)
14            root_y= find(y)
15
16            if root_x==root_y:
17                return False
18            if rank[x]>rank[y]:
19                parent[root_y] = root_x
20            elif rank[x]<rank[y]:
21                parent[root_x] = root_y
22            else:
23                parent[root_y] = root_x
24                rank[root_x]+=1
25            return True
26        
27        for a, b in edges:
28            if not union(a,b):
29                return False
30        return True    
31        