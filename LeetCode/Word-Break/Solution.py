1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        n=len(s)
4        wordDict=set(wordDict)
5
6        @lru_cache(None)
7        def dfs(i): # idx=i-1
8            if i==0:
9                return True
10            for j in range(i):
11                if s[j:i] in wordDict and dfs(j):
12                    return True
13            return False
14        return dfs(n)