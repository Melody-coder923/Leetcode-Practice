1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        @lru_cache(None)
5        def dfs(i):  #dfs(i) = s[0:i+1] 这一段前缀的解码方式数量
6            if i<0:
7                return 1
8            res=0
9            if s[i]!="0":
10                res+=dfs(i-1) 
11            if i-1>=0 and 10<= int(s[i-1:i+1]) <=26:
12                res+=dfs(i-2)
13            return res
14        
15        return dfs(n-1)
16