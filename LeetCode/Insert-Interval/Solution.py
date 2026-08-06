1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        intervals.append(newInterval)
4        intervals.sort()
5        res=[intervals[0]]
6        for start,end in intervals[1:]:
7            if res[-1][1]<start:
8                res.append([start,end])
9            else:
10                res[-1][0]=min(start,res[-1][0])
11                res[-1][1]=max(end,res[-1][1])
12        return res
13            
14