1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        if s[0]=="0":
5            return 0
6
7        @lru_cache(None)
8        def dfs(i):
9            if i<0:
10                return 1
11            res=0
12            if s[i]!="0":
13                res+=dfs(i-1)
14            if i-1>=0 and 10<=int(s[i-1:i+1])<=26:
15                res+=dfs(i-2)
16            return res
17        
18        return dfs(n-1)
19        