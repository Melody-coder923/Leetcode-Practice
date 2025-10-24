class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Edge case
        if len(nums)<=k:
            return list(set(nums))
        res=[]
        #step1: counter 计算频率
        count= Counter(nums)
        min_heap=[]
        #step2: min_heap : (freq, num)    len(min_heap)<k
        for num,freq in count.items():
            if len(min_heap)<k:
                heapq.heappush(min_heap,(freq,num))
            elif min_heap[0][0]<freq:  #heap 全局freq最高得最小堆 (3,1),(2,2)    (4,3)
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(freq,num))
        
        #step3: 搜集结果
        while min_heap:
            freq,num = heapq.heappop(min_heap)
            res.append(num)

        return res
            