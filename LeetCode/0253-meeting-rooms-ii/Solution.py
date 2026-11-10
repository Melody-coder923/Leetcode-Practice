class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        if n==1:
            return 1

        lst=[]
        for start,end in intervals:
            lst.append((start,1))
            lst.append((end,-1))
        
        lst.sort()
        count=0
        res=0
        for time, num in lst:
            count+=num
            res=max(res,count)

        return res
