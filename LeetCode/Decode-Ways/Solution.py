1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        if s[0]=="0":
5            return 0
6        dp=[0]*(n+1)
7        dp[0]=1
8        dp[1]=0 if s[0]=="0" else 1
9        for i in range(2,n+1):
10            if s[i-1]!="0":
11                dp[i]+=dp[i-1]
12            if 10<= int(s[i-2:i])<=26:
13                dp[i]+=dp[i-2]
14        return dp[n]