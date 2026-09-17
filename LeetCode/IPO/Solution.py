1class Solution:
2    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
3        #(profit,capital）: list + sort by capital
4        lst=list(zip(profits,capital))
5       
6        lst.sort(key=lambda x: x[1])
7
8        i=0
9        count=0
10        heap=[]
11        
12        while True:
13            # 装capital<w   (profit,capital） -> heap           
14            while i<len(lst):
15                profit,capital=lst[i]
16
17                if capital<=w:
18                    heapq.heappush(heap,(-profit))
19                else:
20                    break
21                i+=1
22            
23            # 如果当前capital no projec could invest :break
24            if not heap:
25                break
26
27            # heap pop  count<k, change w
28            neg_profit=heapq.heappop(heap)
29            w-=neg_profit
30
31            count+=1
32            if count==k:
33                break
34        
35        return w
36
37            
38        
39