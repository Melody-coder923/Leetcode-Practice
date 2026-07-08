1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        from collections import deque,defaultdict
4        graph=defaultdict(list)
5        for u,v,w in times:
6            graph[u].append((w,v))
7        heap=[(0,k)]
8        dist={}
9        while heap:
10            d,u=heapq.heappop(heap)
11            if u in dist:
12                continue
13            dist[u]=d
14        
15            for w,v in graph[u]:
16                if v not in dist:
17                    heapq.heappush(heap,(d+w,v))
18
19        if len(dist)<n:
20            return -1
21        else:
22            return max(dist.values())
23             