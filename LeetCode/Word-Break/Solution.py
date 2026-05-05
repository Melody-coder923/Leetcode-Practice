1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        n=len(s)
4        wordDict=set(wordDict)
5        @lru_cache(None)
6        def dfs(i):
7            if i==0:
8                return True
9            
10            for j in range(i):
11                if s[j:i] in wordDict and dfs(j):
12                    return True
13            return False
14        
15        return dfs(n)
16