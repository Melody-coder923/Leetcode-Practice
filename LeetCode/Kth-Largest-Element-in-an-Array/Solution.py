1import random
2
3class Solution:
4    def findKthLargest(self, nums: List[int], k: int) -> int:
5        min_heap = []
6        for num in nums:
7            heapq.heappush(min_heap, num)
8            if len(min_heap) > k:
9                heapq.heappop(min_heap)
10        return min_heap[0]