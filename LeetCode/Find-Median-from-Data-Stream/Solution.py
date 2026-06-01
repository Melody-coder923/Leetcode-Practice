1import heapq
2class MedianFinder:
3
4    def __init__(self):
5        self.max_heap = []  # left half (as max heap)
6        self.min_heap = []  # right half (as min heap)
7
8    def addNum(self, num: int) -> None:
9        heapq.heappush(self.max_heap, -num)
10
11        # 保证 max_heap 的最大值 <= min_heap 的最小值
12        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
13
14        # 如果两边不平衡，调整一下：max_heap 要比 min_heap 至多多一个元素
15        if len(self.min_heap) > len(self.max_heap):
16            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
17
18    def findMedian(self) -> float:
19        if len(self.max_heap) > len(self.min_heap):
20            return -self.max_heap[0]
21        else:
22            return (-self.max_heap[0] + self.min_heap[0]) / 2
23
24
25# Your MedianFinder object will be instantiated and called as such:
26# obj = MedianFinder()
27# obj.addNum(num)
28# param_2 = obj.findMedian()