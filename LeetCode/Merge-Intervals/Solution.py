1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        prev_end=intervals[0][-1]
5        res=[intervals[0]]
6        for start,end in intervals[1:]:
7            if start>prev_end:
8                res.append([start,end])
9            else:
10                res[-1][1]=max(end,res[-1][1])
11            prev_end=res[-1][-1]
12        
13        return res
14