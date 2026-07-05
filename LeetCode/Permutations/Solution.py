1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res=[]
4        nums.sort()
5        used=[False]*len(nums)
6        path=[]
7        def backtrack():
8            if len(path)==len(nums):
9                res.append(path[:])
10                return
11            for i in range(len(nums)):
12                if  not used[i]:
13                    path.append(nums[i])
14                    used[i]=True
15                    backtrack()
16                    path.pop()
17                    used[i]=False
18        backtrack()
19        return res
20                
21
22                    