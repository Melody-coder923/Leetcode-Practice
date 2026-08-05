1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        parents=list(range(n)) #[0,1,2,3,5]
4
5        def find(x):
6            if parents[x]!=x:
7                parents[x]=find(parents[x])
8            return parents[x]
9        
10        def union(x,y):
11            root_x=find(x)
12            root_y=find(y)
13            if root_x==root_y:
14                return False
15            
16            else:
17                parents[root_y]=root_x
18                return True
19        
20        
21        for u,v in edges:
22            if union(u,v):
23                n-=1
24        
25        return n
26
27