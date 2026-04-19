1class SmallestInfiniteSet:
2
3    def __init__(self):
4        # set check if it already in the set
5        self.num_set=set() # 放add back 数，功能是查重复
6        self.smallest=1  # 原始的最小的1
7        self.min_heap=[] #放add back 数
8
9    def popSmallest(self) -> int:
10        if self.min_heap:
11            num=heapq.heappop(self.min_heap)
12            self.num_set.remove(num)
13            return num
14        else:
15            self.smallest+=1
16            return self.smallest-1
17        
18    def addBack(self, num: int) -> None:
19        if num not in self.num_set and num <self.smallest:
20            heapq.heappush(self.min_heap,num) #min_heap [3]
21            self.num_set.add(num)  #num_set [3]
22 
23# Your SmallestInfiniteSet object will be instantiated and called as such:
24# obj = SmallestInfiniteSet()
25# param_1 = obj.popSmallest()
26# obj.addBack(num)