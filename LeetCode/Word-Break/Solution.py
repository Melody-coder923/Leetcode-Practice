1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        wordDict=set(wordDict)
4        n=len(s)
5        dp=[False]*(n+1)
6        dp[0]=True
7        for i in range(n+1):
8            for j in range(i):
9                if dp[j] and s[j:i] in wordDict:
10                    dp[i]=True
11                    break
12        return dp[n]         