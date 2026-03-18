1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        min_heap = []
4        for num in nums:
5            heapq.heappush(min_heap, num)
6            if len(min_heap) > k:
7                heapq.heappop(min_heap)
8        return min_heap[0]