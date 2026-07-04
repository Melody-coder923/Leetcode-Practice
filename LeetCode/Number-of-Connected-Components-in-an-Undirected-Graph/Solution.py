1from typing import List
2
3class Solution:
4    def countComponents(self, n: int, edges: List[List[int]]) -> int:
5        parent = [i for i in range(n)]
6
7        def find(x):
8            while parent[x] != x:
9                parent[x] = parent[parent[x]]  # 路径压缩
10                x = parent[x]
11            return x
12
13        def union(a, b):
14            rootA = find(a)
15            rootB = find(b)
16            if rootA == rootB:
17                return False  # 已经连接，没减少连通分量
18            parent[rootB] = rootA
19            return True
20
21        count = n
22        for a, b in edges:
23            if union(a, b):
24                count -= 1  # 合并成功，连通分量减一
25
26        return count