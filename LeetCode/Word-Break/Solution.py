1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        wordDict=set(wordDict)
4        n=len(s)
5        @lru_cache(None)
6        def dfs(i):
7            if i==0:
8                return True
9            for j in range(i):
10                if s[j:i] in wordDict and dfs(j):
11                    return True
12                
13            return False
14        return dfs(n)