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
23            # heap pop  count<k, change w
24            if not heap:
25                break
26
27            neg_profit=heapq.heappop(heap)
28            w-=neg_profit
29
30            count+=1
31            if count==k:
32                break
33        
34        return w
35
36            
37        
38