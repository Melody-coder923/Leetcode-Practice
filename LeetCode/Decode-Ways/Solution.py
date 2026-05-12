1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        dp= [0]* (n+1)
5        dp[0]=1
6
7        for i in range(1,n+1):
8            if s[i-1]!="0":
9                dp[i]+= dp[i-1]
10            if i-2>=0 and 10<=int(s[i-2:i])<=26:
11                dp[i]+= dp[i-2]
12        
13        return dp[n]