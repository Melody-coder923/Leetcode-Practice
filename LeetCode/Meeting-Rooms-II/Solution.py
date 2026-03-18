1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        lst=[]
4        for start,end in intervals:
5            lst.append((start,1))
6            lst.append((end,-1))
7        
8        lst.sort()
9        max_rooms=0
10        res=0
11        for time,room in lst:
12            res+=room
13            max_rooms = max(max_rooms, res)
14        return max_rooms
15            