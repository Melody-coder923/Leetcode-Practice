1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        graph=defaultdict(list)
4        for u,v,w in times:
5            graph[u].append((w,v))
6           
7        heap=[(0,k)]
8        map={}
9        while heap:
10            dis,node=heapq.heappop(heap)
11            if node in map:
12                continue
13            map[node]=dis
14        
15            for w,v in graph[node]:
16                if v not in map:
17                    heapq.heappush(heap,(dis+w,v))
18
19        if len(map)<n:
20            return -1
21        else:
22            return max(map.values())