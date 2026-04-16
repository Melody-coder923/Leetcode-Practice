1class Solution:
2    def minReorder(self, n: int, connections: List[List[int]]) -> int:
3        graph=defaultdict(list)
4        for a,b in connections:
5            graph[a].append((b,1))
6            graph[b].append((a,0))
7        visited=set()
8        def dfs(node):
9            visited.add(node)
10            changes=0
11            visited.add(node)
12            for nei, need_change in graph[node]:
13                if nei not in visited:
14                    changes+=need_change
15                    changes+=dfs(nei)
16            return changes
17        return dfs(0)
18        
19
20
21
22