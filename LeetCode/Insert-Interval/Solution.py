1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        # merge
4        intervals.append(newInterval)
5
6        n=len(intervals)
7        if n<=1:
8            return intervals
9
10        # start sort,  overlap
11        #[1,3] [2,5] [6,9]
12        intervals.sort()
13
14        res=[intervals[0]] #res=[[1,5],[6,9]]
15
16        for i in range(1,n):
17            #overlap
18            if intervals[i][0]<=res[-1][1]:
19                res[-1][0]=min(intervals[i][0],res[-1][0])
20                res[-1][1]=max(intervals[i][1],res[-1][1])
21                
22            else:
23                res.append(intervals[i])
24
25        return res
26
27            
28