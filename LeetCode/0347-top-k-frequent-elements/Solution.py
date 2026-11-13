class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count=Counter(nums) # num: freq
        heap=[] 

        for num,freq in count.items():
            if len(heap)<k:
                heapq.heappush(heap,(freq,num))
            else:
                if heap[0][0]<freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(freq,num))

        res=[]
        while heap:
            _, num=heapq.heappop(heap)
            res.append(num)

        return res