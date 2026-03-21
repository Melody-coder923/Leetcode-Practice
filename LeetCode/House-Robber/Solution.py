1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        if n == 0:
5            return 0
6        if n == 1:
7            return nums[0]
8        dp=[0]*n
9        dp[0]=nums[0]
10        dp[1] = max(nums[0], nums[1])
11        
12        for i in range(2,n):
13            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
14        return dp[n-1]
15
16
17