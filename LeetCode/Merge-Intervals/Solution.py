1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        prev=intervals[0]
5        res=[]
6        for start,end in intervals[1:]:
7            if start>prev[1]:
8                res.append(prev)
9                prev=[start,end]
10            else:
11                prev[1]=max(prev[1],end)
12        res.append(prev)
13        return res
14