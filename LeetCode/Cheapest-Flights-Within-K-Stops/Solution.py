1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int: 
3        dist = [float("inf")] * n
4        dist[src] = 0
5        for i in range(k + 1):
6            tmp = dist[:]
7            for u, v, w in flights:
8                if dist[u] != float("inf") and dist[u] + w < tmp[v]:  # ✅ 用 tmp[v] 判断和更新
9                    tmp[v] = dist[u] + w
10            dist=tmp
11        return -1 if dist[dst] == float("inf") else dist[dst]
12            