1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int: 
3        n=len(nums)
4        if n <= 1:
5            return n
6        dp=[1]*n
7        dp[0]=1
8        res=1
9        for i in range(1,n):
10            for j in range(i):
11                if nums[i]>nums[j]:
12                    dp[i]=max(dp[i],dp[j]+1)
13            res=max(res,dp[i])
14        return res