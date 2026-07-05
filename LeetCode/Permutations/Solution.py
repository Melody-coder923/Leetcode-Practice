1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res=[]
4        nums.sort()
5        used=[False]*len(nums)
6        path=[]
7        def backtracking():
8            if len(path)==len(nums):
9                res.append(path[:])
10                return
11            for i in range(len(nums)):
12                if used[i]:
13                    continue 
14                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
15                    continue
16                path.append(nums[i])
17                used[i]=True
18                backtracking()
19                path.pop()
20                used[i]=False
21        backtracking()
22        return res