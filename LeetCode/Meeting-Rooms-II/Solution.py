1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        lst=[]
4        for start,end in intervals:
5            lst.append((start,1))
6            lst.append((end,-1))
7        
8        lst.sort()
9
10        res=0
11        maxroom=0
12        for time,count in lst:
13            res+=count
14            maxroom=max(res,maxroom)
15        return maxroom