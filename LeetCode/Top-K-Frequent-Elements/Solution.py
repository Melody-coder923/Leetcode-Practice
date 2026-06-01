1from collections import Counter
2class Solution:
3    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
4        min_heap=[]
5        count=Counter(nums)
6        for value,freq in count.items():
7                if len(min_heap)<k:
8                    heapq.heappush(min_heap,(freq,value))
9                elif min_heap[0][0]<freq:
10                        heapq.heappop(min_heap)
11                        heapq.heappush(min_heap,(freq,value))
12        res=[]
13        while min_heap:
14            freq,value=heapq.heappop(min_heap)
15            res.append(value)
16        return res
17        
18       