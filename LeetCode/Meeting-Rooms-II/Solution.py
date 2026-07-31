1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        """
4                0                30
5                5  10 
6                        15. 20
7                
8                +1 +1 -1. +1. -1 -1
9                0 1
10                5 1
11                10 -1
12                15 1
13                20 -1
14                30 -1 
15        """
16        room=0
17        res=[]
18        min_room=0
19        for start,end in intervals:
20            res.append((start,1))
21            res.append((end,-1))
22        res.sort()
23        for time, count in res:
24            room+=count
25            min_room=max(room,min_room)
26        
27        return min_room
28            
29       
30
31      