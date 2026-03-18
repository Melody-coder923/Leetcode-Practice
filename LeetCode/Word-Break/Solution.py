1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        
4        wordDict=set(wordDict)
5        n=len(s)
6        dp=[False]*(n+1)
7        dp[n]=True
8        for i in range(n-1,-1,-1):
9            for j in range(i+1,n+1):
10                if s[i:j] in wordDict and dp[j]:
11                    dp[i]=True
12        return dp[0]