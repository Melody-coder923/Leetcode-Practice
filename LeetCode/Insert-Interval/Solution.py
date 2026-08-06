1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        intervals.sort()
4        res=[]
5        for start,end in intervals:
6        #new在后面
7            if end<newInterval[0]:
8                res.append([start,end])
9        #new在前面
10            elif start>newInterval[1]:
11                res.append(newInterval)
12                newInterval = [start, end]
13            else:
14                newInterval[0]=min(newInterval[0],start)
15                newInterval[1] = max(newInterval[1], end)
16        res.append(newInterval)
17        return res
18