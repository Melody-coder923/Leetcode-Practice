1class Solution:
2    def minReorder(self, n: int, connections: List[List[int]]) -> int:
3        from collections import defaultdict
4        graph = defaultdict(list)
5        for a, b in connections:
6            graph[a].append((b, 1))
7            graph[b].append((a, 0))
8        visited = set()
9        def dfs(node):
10            visited.add(node)
11            changes = 0
12            for neighbor, needs_change in graph[node]:
13                if neighbor not in visited:
14                    changes += needs_change
15                    changes += dfs(neighbor)
16            return changes
17        return dfs(0)