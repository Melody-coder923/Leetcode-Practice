1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res = []
4
5        for start, end in intervals:
6            # 情况1：当前区间在 newInterval 左边
7            if end < newInterval[0]:
8                res.append([start, end])
9
10            # 情况2：当前区间在 newInterval 右边
11            elif start > newInterval[1]:
12                res.append(newInterval)
13                newInterval = [start, end]
14
15            # 情况3：有重叠，合并到 newInterval
16            else:
17                newInterval[0] = min(newInterval[0], start)
18                newInterval[1] = max(newInterval[1], end)
19
20        res.append(newInterval)
21        return res
22
23
24