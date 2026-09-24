1class Solution:
2    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
3        res=[]
4        n=len(nums)
5        nums.sort()
6
7        def backtrack(start,path):
8            res.append(path[:])
9            for i in range(start,n):
10                # check repeat
11                if i>start and nums[i]==nums[i-1]:
12                    continue
13                path.append(nums[i])
14                backtrack(i+1,path)
15                path.pop()
16
17        backtrack(0,[])
18        return res