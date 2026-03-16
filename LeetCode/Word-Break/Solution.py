1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        n=len(s)
4        dp=[False]*(n+1)
5        dp[0]=True
6        for i in range(1,n+1):
7            for j in range(i):
8                if dp[j] and s[j:i] in wordDict:
9                    dp[i]=True
10        return dp[n]
11