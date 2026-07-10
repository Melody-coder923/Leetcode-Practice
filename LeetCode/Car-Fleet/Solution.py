1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        """
4        情况1:time=(target-position)//speed
5        情况2: 在到target前相遇
6        后车到 target 的时间 <= 前车到 target 的时间
7
8
9        情况 1：后车追不上前车
10        后车时间 > 前车时间
11
12        情况 2：后车能追上前车
13        后车时间 <= 前车时间
14        """
15
16        cars = sorted(zip(position, speed), reverse=True)
17
18        fleets = 0
19        slowest_time = 0
20
21        for pos, spd in cars:
22            time = (target - pos) / spd
23
24            if time > slowest_time:
25                fleets += 1
26                slowest_time = time
27
28        return fleets