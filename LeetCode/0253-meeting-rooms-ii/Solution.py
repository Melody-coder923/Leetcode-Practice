class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        n=len(intervals)
        if n<=1:
            return n

        lst=[]
        for start,end in intervals:
            lst.append((start,1))
            lst.append((end,-1))

        lst.sort()

        res=cur=0
        for time, count in lst:
            cur+=count
            res=max(res,cur)


        return res
