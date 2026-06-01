1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        lst=[]
4        for start,end in intervals:
5            lst.append((start,1))
6            lst.append((end,-1))
7        
8        lst.sort()
9        res=0
10        maxmeeting=0
11        for time,cal in lst:
12            res+=cal
13            maxmeeting=max(maxmeeting,res)
14        return maxmeeting
15        
16
17
18            