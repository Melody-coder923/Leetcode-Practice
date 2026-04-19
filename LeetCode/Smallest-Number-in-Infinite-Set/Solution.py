1import heapq
2class SmallestInfiniteSet:
3
4    def __init__(self):
5        self.current_num =1
6        self.min_heap = []
7        self.heap_elements_set = set()
8
9    def popSmallest(self) -> int:
10        if self.min_heap:
11            smallest = heapq.heappop(self.min_heap)
12            self.heap_elements_set.remove(smallest)
13            return smallest
14        else:
15            smallest = self.current_num
16            self.current_num +=1
17            return smallest
18
19
20    def addBack(self, num: int) -> None:
21        if num < self.current_num:
22            if num not in self.heap_elements_set:
23                heapq.heappush(self.min_heap, num)
24                self.heap_elements_set.add(num)   
25
26
27# Your SmallestInfiniteSet object will be instantiated and called as such:
28# obj = SmallestInfiniteSet()
29# param_1 = obj.popSmallest()
30# obj.addBack(num)