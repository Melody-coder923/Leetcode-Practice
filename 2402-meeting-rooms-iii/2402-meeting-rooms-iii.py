import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #按会议开始时间遍历每个会议,释放空闲房间
        #分配房间:有空闲房间,无空闲房间
        freerooms=[i for i in range(n)] #room_id
        heapq.heapify(freerooms)
        userooms=[] #(end_time, room_id)
        room_count= [0]*n
        meetings.sort(key=lambda x: x[0])
        for start,end in meetings:
            while userooms and userooms[0][0] <= start:
                _, room_id = heapq.heappop(userooms)
                heapq.heappush(freerooms, room_id)
            duration= end-start
            if freerooms:
                room_id = heapq.heappop(freerooms)
                actual_end = start + duration
            else:
                prev_end, room_id = heapq.heappop(userooms)
                actual_end = prev_end + duration  # 延迟会议结束时间
            
            heapq.heappush(userooms, (actual_end, room_id))
            room_count[room_id] += 1
        maxcount=0
        for i, count in enumerate(room_count):
            if count>maxcount:
                maxcount=count
                res=i
        return res



        
