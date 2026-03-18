1import heapq
2class Solution:
3    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
4        freq=[0] *n
5        available=list(range(n))
6        heapq.heapify(available)
7        occupy=[]
8        
9        meetings.sort()
10        for start,end in meetings:
11            # 先释放所有已经结束的房间
12            while occupy and occupy[0][0] <= start:
13                _, room_id= heapq.heappop(occupy)
14                heapq.heappush(available, room_id)
15            
16            duration= end-start
17            if available: # 有空闲房间，直接安排
18                room_id=heapq.heappop(available)
19                actual_end =end
20            else: # 没有空闲房间，等最早结束的那个
21                prev_end, room_id = heapq.heappop(occupy)
22                actual_end = prev_end + duration  # 延迟会议结束时间
23            
24            heapq.heappush(occupy, (actual_end, room_id))
25            freq[room_id] += 1
26        maxcount=max(freq)
27        for i, count in enumerate(freq):
28            if count == maxcount:
29                return i
30        
31
32
33                    
34                
35