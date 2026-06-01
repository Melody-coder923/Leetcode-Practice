1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x: x[1])
4        last=intervals[0] 
5        count=1
6        for interval in intervals[1:]:
7            if interval[0]>=last[1]:
8                count+=1
9                last=interval
10        return len(intervals)-count