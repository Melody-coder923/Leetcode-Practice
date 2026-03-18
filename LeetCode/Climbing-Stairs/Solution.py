1class Solution:
2    def climbStairs(self, n: int) -> int:
3        dp=[0]*(n+1)
4        dp[0]=1
5        dp[1]=1
6        for i in range(2,n+1):
7            dp[i]=dp[i-1]+dp[i-2]
8        
9        return dp[n]