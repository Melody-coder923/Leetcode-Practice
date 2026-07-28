1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        n=len(intervals)
4        if n<=1:
5            return True
6        # 开始时间排序
7        intervals.sort()
8        #比较对象
9        prev_end=intervals[0][1]
10        for start,end in intervals[1:]:
11            if start<prev_end:
12                return False
13            prev_end=end
14        return True