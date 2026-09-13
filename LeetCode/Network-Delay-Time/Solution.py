1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        dict=defaultdict(list)
4        for u,v,w in times:
5            dict[u].append((w,v))
6        
7
8        heap=[]
9        distances=[float("inf")]*(n+1)
10        distances[k]=0
11        heapq.heappush(heap,(0,k))
12
13        while heap:
14            cur_dis,node= heapq.heappop(heap)
15            if cur_dis>distances[node]:
16                continue
17            
18            for w,nei in dict[node]:
19                new_dist = cur_dis + w
20                if new_dist<distances[nei]:
21                    distances[nei] = new_dist
22                    heapq.heappush(heap,(new_dist,nei))
23
24        ans = max(distances[1:])
25        return ans if ans != float("inf") else -1