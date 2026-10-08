1class Solution:
2    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
3        wordDict=set(wordDict)
4        n=len(s)
5
6        @lru_cache(None)
7        def dfs(i):
8            #base case
9            if i==0:
10                return True 
11
12            for j in range(i):
13                if s[j:i] in wordDict and dfs(j):
14                    return True
15
16            return False
17            
18        return dfs(n)