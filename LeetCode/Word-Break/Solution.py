1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        memo={}
4        wordDict=set(wordDict)
5        n=len(s)
6        def dfs(i):
7            #base case
8            if i==n:
9                return True
10            #memo
11            if i in memo:
12                return memo[i]
13            # break big into small to check repeat area
14            for j in range(i+1,n+1):
15                if s[i:j] in wordDict and dfs(j):
16                    memo[i]=True
17                    return True
18            # keep memo
19            memo[i]=False
20            return False
21
22        return dfs(0)