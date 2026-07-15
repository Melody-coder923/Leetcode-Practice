1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        if not intervals:
4            return 0
5        intervals.sort(key=lambda x: x[1])
6        prev=intervals[0][-1]
7        kept = 1
8        n=len(intervals)
9        for start,end in intervals[1:]:
10            if start>=prev:
11                kept+=1
12                prev=end
13        
14        return n-kept