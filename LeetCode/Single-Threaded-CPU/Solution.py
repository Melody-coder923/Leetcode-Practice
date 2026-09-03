1class Solution:
2    def getOrder(self, tasks: List[List[int]]) -> List[int]:
3        # lst= (enqueueTime, processingTime,id)
4        lst=[]
5        for id in range(len(tasks)):
6            enqueueTime,processingTime=tasks[id]
7            lst.append((enqueueTime,processingTime,id))
8 
9        # enqueueTime -sort: 
10        lst.sort()
11
12        # time
13        time=0
14        i=0
15        heap=[]
16        res=[]
17        
18        # for/while lst
19        while i <len(lst) or heap:
20            # CPU 空闲，而且下一个任务还没到达
21            if not heap and time < lst[i][0]:
22                time = lst[i][0]
23
24            # enqueueTime<= time   into heap  ( processingTime, id )
25            while i < len(lst) and lst[i][0] <= time:
26                enqueue_time, processing_time, task_id = lst[i]
27                heapq.heappush(heap,(processing_time,task_id))  
28                i+=1
29
30            #pop
31            processing_time,task_id= heapq.heappop(heap)
32            res.append(task_id)
33            time+=processing_time
34
35        return res