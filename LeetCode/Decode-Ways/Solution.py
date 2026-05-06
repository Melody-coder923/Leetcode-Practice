1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        dp= [0]* (n+1)
5        dp[0]=1
6        for i in range(1,n+1):
7            if s[i - 1] != "0":
8                dp[i]+=dp[i-1]
9            if i >= 2:
10                twodigit = int(s[i-2:i])
11                if 10<=twodigit<=26:
12                    dp[i]+=dp[i-2]
13        return dp[n]