1class Solution:
2    from collections import Counter
3    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
4        #Edge case
5        if len(nums)<=k:
6            return list(set(nums))
7        res=[]
8        #step1: counter 计算频率
9        count= Counter(nums)
10        min_heap=[]
11        #step2: min_heap : (freq, num)    len(min_heap)<k
12        for num,freq in count.items():
13            if len(min_heap)<k:
14                heapq.heappush(min_heap,(freq,num))
15            elif min_heap[0][0]<freq:  #heap 全局freq最高得最小堆 (3,1),(2,2)    (4,3)
16                    heapq.heappop(min_heap)
17                    heapq.heappush(min_heap,(freq,num))
18        
19        #step3: 搜集结果
20        while min_heap:
21            freq,num = heapq.heappop(min_heap)
22            res.append(num)
23
24        return res
25            
26
27