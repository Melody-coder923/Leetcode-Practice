1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        n=len(s)
4        dp=[False]*(n+1)
5        dp[0]=True
6        wordDict=set(wordDict)
7
8        for i in range(1,n+1):
9            for j in range(i): 
10                if s[j:i] in wordDict and dp[j]:
11                    dp[i]=True
12        return dp[n]