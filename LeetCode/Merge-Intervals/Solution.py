1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        n=len(intervals)
4        if n<=1:
5            return intervals
6        intervals.sort()
7        res=[intervals[0]]
8        for i in range(1,n):
9            #overlap
10            if intervals[i][0]<=res[-1][1]:
11                res[-1][0]=min(intervals[i][0],res[-1][0])
12                res[-1][1]=max(intervals[i][1],res[-1][1])
13
14            #non-overlap
15            else:
16                res.append(intervals[i])
17        
18        return res
19
20