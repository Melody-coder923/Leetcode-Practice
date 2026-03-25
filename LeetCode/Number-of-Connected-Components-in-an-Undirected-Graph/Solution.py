1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        map=defaultdict(list)
4        for u,v in edges:
5            map[u].append(v)
6            map[v].append(u)
7        visited=set()
8        def dfs(node):
9            visited.add(node)
10            for nei in map[node]:
11                if nei not in visited:
12                    dfs(nei)
13            return visited
14
15        count=0
16        for i in range(n):
17            if i not in visited:
18                dfs(i)
19                count+=1
20        return count