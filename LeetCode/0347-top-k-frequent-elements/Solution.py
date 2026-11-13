class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num in count:
            freq = count[num]

            if len(heap) < k:
                heapq.heappush(heap, (freq, num))

            elif heap[0][0] < freq:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))

        res = []

        while heap:
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res
        