1class Solution:
2    def climbStairs(self, n: int) -> int:
3        #edge case
4        if n<=2:
5            return n
6        # 定义：1维/2维，什么是dp[i]
7        #dp[i]: 到i位置有多少方法 
8        dp= [0] * (n+1) 
9        # base case 
10        a=1
11        b=2
12        # update the dp matrix
13        for i in range(3,n+1):
14            cur = a + b
15            a = b
16            b = cur
17        return b
18      