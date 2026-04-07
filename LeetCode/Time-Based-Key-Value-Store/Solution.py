1class TimeMap:
2
3    def __init__(self):
4        self.map = {}   # key -> list of [timestamp, value]
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.map:
8            self.map[key] = []
9        self.map[key].append([timestamp, value])
10
11    def get(self, key: str, timestamp: int) -> str:
12        if key not in self.map:
13            return ""
14        arr = self.map[key]
15        left, right = 0, len(arr) - 1
16        ans = ""
17        while left <= right:
18            mid = (left + right) // 2
19
20            if arr[mid][0] <= timestamp:
21                ans = arr[mid][1]
22                left = mid + 1
23            else:
24                right = mid - 1
25
26        return ans
27        
28
29
30# Your TimeMap object will be instantiated and called as such:
31# obj = TimeMap()
32# obj.set(key,value,timestamp)
33# param_2 = obj.get(key,timestamp)