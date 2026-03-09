1class HitCounter:
2
3    def __init__(self):
4        self.hits=[]
5
6    def hit(self, timestamp: int) -> None:
7        self.hits.append(timestamp)
8        
9
10    def getHits(self, timestamp: int) -> int:
11        target=timestamp-300
12        left, right = 0, len(self.hits)
13
14        while left < right:
15            mid = (left + right) // 2
16            if self.hits[mid] <= target:
17                left = mid + 1
18            else:
19                right = mid
20
21        return len(self.hits) - left
22
23
24# Your HitCounter object will be instantiated and called as such:
25# obj = HitCounter()
26# obj.hit(timestamp)
27# param_2 = obj.getHits(timestamp)