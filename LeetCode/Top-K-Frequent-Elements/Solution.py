1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count=Counter(nums)
4
5        heap=[]
6        for num,fre in count.items():
7            heapq.heappush(heap,(-fre,num))
8        res=[]
9        while k>0 and heap:
10            freq,num= heapq.heappop(heap)
11            res.append(num)
12            k-=1
13        
14        return res
15        
16