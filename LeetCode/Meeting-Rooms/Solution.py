1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        if not intervals:
4            return True
5        intervals.sort()
6        prev=intervals[0][1]
7        for start,end in intervals[1:]:
8            if prev>start:
9                return False
10            prev=max(prev,end)
11        
12        return True
13