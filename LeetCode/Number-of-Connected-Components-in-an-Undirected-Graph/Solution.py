1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        # build relation- dict  node -[]
4        dict=defaultdict(list)
5        for u,v in edges:
6            dict[u].append(v)
7            dict[v].append(u)
8
9        # dfs  visited -group
10        visited=set()
11
12        def dfs(node):
13            visited.add(node)
14            for nei in dict[node]:
15                if nei not in visited:
16                    dfs(nei)
17    
18
19        # for +dfs -> group +1
20        group=0
21        for node in range(n):
22            if node not in visited:
23                dfs(node)
24                group+=1
25        
26        return group