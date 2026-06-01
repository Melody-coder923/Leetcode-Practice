1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res=[]
4        n_s=newInterval[0]
5        n_e=newInterval[1]
6        for start,end in intervals:
7            if end<n_s:
8                res.append([start,end])
9            elif start>n_e:     
10                res.append([n_s,n_e])
11                n_s=start
12                n_e=end
13            else:
14                n_s=min(start,n_s)
15                n_e=max(end,n_e)
16        res.append([n_s,n_e])
17        return res
18
19      