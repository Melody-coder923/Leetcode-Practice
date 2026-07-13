1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        wordDict=set(wordDict)
4        n=len(s)
5        @lru_cache(None)
6        def dfs(i):
7            if i == 0:
8                return True
9            for j in range(i):
10                if s[j:i] in wordDict:
11                    if dfs(j):
12                        return True
13            return False
14        
15        return dfs(n)
16            
17