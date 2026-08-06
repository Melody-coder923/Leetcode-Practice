1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        #intervals = [[1,3],[6,9]], newInterval = [2,5]
4        res=[]
5        for i in range(len(intervals)):
6            #前面
7            if newInterval[1]<intervals[i][0]:
8                res.append(newInterval)
9                res.extend(intervals[i:])
10                return res
11            #重合
12            elif newInterval[0]<=intervals[i][1]:
13                newInterval[0]=min(intervals[i][0],newInterval[0])
14                newInterval[1]=max(intervals[i][1],newInterval[1])
15            #后面
16            else:
17                res.append(intervals[i])
18        
19        res.append(newInterval)
20
21        return res
22
23    