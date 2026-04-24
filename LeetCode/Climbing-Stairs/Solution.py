1class Solution:
2    def climbStairs(self, n: int) -> int:
3        #edge case
4        if n<=2:
5            return n
6        # 定义：1维/2维，什么是dp[i]
7        #dp[i]: 到i位置有多少方法 
8        dp= [0] * (n+1) 
9        # base case 
10        dp[0]=1
11        dp[1]=1
12        dp[2]=2
13        # update the dp matrix
14        for i in range(3,n+1):
15            dp[i]=dp[i-1]+dp[i-2]
16        # res(check and return )
17        return dp[n]