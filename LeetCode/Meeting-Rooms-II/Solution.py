1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        # 按开始时间排序
4        intervals.sort(key=lambda x: x[0])
5        
6        # 最小堆存储会议结束时间
7        heap = []
8        
9        for interval in intervals:
10            start, end = interval
11            
12            # 如果当前会议开始时间>=堆顶结束时间，可以复用会议室
13            if heap and start >= heap[0]:
14                heapq.heappop(heap)
15            
16            # 将当前会议结束时间加入堆
17            heapq.heappush(heap, end)
18        
19        return len(heap)
20