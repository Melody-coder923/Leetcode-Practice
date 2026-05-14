1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        if n>=1 and s[0]=="0":
5            return 0
6        @lru_cache(None)
7        def dfs(i):
8            if i==-1:
9                return 1
10            res=0
11            if s[i]!="0":
12                res+=dfs(i-1)
13            if i-1>=0 and 10<=int(s[i-1:i+1])<=26:
14                res+=dfs(i-2)
15            return res
16            
17        return  dfs(n-1)