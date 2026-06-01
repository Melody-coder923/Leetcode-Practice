1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        if len(intervals)==1:
4            return 1
5        events=[]
6        count=0
7        for start,end in intervals:
8            events.append((start,1))
9            events.append((end,-1))
10        events.sort(key=lambda x: (x[0], x[1]))
11        current_rooms = 0
12        max_rooms=0
13        for time, event in events:
14            current_rooms += event
15            max_rooms = max(max_rooms, current_rooms)
16        return max_rooms
17