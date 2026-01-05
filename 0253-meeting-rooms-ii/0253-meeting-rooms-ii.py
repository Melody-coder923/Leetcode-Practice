class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        lst=[]
        for start,end in intervals:
            lst.append((start,1))
            lst.append((end,-1))
        
        lst.sort()
        max_rooms=0
        res=0
        for time,room in lst:
            res+=room
            max_rooms = max(max_rooms, res)
        return max_rooms
            