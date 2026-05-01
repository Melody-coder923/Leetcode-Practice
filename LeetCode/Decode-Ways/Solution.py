1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        @lru_cache(None)
5        def dfs(i):
6            if i == 0:
7                return 1 if s[0] != "0" else 0
8            res=0
9            if s[i]!="0":
10                res+=dfs(i-1)
11            
12            if i - 1 >= 0 and 10 <= int(s[i-1:i+1]) <= 26:
13                if i == 1:
14                    res += 1
15                else:
16                    res += dfs(i - 2)
17
18            return res
19        return dfs(n-1)
20            