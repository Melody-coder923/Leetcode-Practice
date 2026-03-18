1import heapq
2class Solution:
3    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
4        #按会议开始时间遍历每个会议,释放空闲房间
5        #分配房间:有空闲房间,无空闲房间
6        freerooms=[i for i in range(n)] #room_id
7        heapq.heapify(freerooms)
8        userooms=[] #(end_time, room_id)
9        room_count= [0]*n
10        meetings.sort(key=lambda x: x[0])
11        for start,end in meetings:
12            while userooms and userooms[0][0] <= start:
13                _, room_id = heapq.heappop(userooms)
14                heapq.heappush(freerooms, room_id)
15            duration= end-start
16            if freerooms:
17                room_id = heapq.heappop(freerooms)
18                actual_end = start + duration
19            else:
20                prev_end, room_id = heapq.heappop(userooms)
21                actual_end = prev_end + duration  # 延迟会议结束时间
22            
23            heapq.heappush(userooms, (actual_end, room_id))
24            room_count[room_id] += 1
25        maxcount=0
26        for i, count in enumerate(room_count):
27            if count>maxcount:
28                maxcount=count
29                res=i
30        return res
31
32
33
34        
35