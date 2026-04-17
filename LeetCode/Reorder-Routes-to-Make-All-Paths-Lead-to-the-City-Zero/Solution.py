1class Solution:
2    def minReorder(self, n: int, connections: List[List[int]]) -> int:
3        #input: connections a->b , n: how many cities, no cycle
4        #output: how many edges should be changed in order to ensure all cities could get to zero   
5        # first: to know the directions +1, 0
6        #change: -> 
7        # graph dict key a : value b
8
9        graph=defaultdict(list)
10        for a,b in connections:
11            graph[a].append((b, 1))
12            graph[b].append((a,0))
13        visited=set()
14        changes=0
15        def dfs(node,visited): #return changes
16            nonlocal changes
17            visited.add(node)
18            for nei,dis in graph[node]:
19                if nei not in visited:
20                    changes+=dis
21                    dfs(nei,visited)
22        dfs(0,visited)
23        return changes
24
25        # 0 
26        #visited {0}
27        # nei in graph[0]
28        # 0 -> nei [ddd]
29
30