1class Solution:
2    def reorganizeString(self, s: str) -> str:
3        count=Counter(s)
4        if (len(s)+1)//2< max(count.values()):
5            return ""
6        maxheap=[]
7        for char,freq in count.items():
8            heapq.heappush(maxheap,(-freq,char))
9
10        res=[]
11        while len(maxheap)>1:
12            freq1,char1=heapq.heappop(maxheap)
13            freq2,char2=heapq.heappop(maxheap)
14            res.append(char1)
15            res.append(char2)
16            if freq1+1<0:
17                heapq.heappush(maxheap,(freq1+1,char1))
18            if freq2+1<0:
19                heapq.heappush(maxheap,(freq2+1,char2))
20        if maxheap:
21            freq,char= heapq.heappop(maxheap)
22            res.append(char)
23        
24        return "".join(res)