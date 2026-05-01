1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        @lru_cache(None)
5        def dfs(i):
6            if i == n:
7                return 1
8            res = 0
9            if s[i] != '0':
10                res += dfs(i + 1)
11            if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
12                res += dfs(i+2)
13            return res
14        return dfs(0)
15            