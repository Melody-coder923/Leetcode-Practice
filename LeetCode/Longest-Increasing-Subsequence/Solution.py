1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        n=len(nums)
4        @lru_cache(None)
5        def dfs(i):
6            res=1
7            for j in range(i):
8                if nums[i]>nums[j]:
9                    res= max(dfs(j)+1,res)
10            return res
11        res=1
12        for i in range(1,n):
13           res=max(res,dfs(i))
14        return res