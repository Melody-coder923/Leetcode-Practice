1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        if n==1 and s[0]!="0":
5            return 1
6        if s[0]=="0":
7            return 0
8
9        @lru_cache(None)
10        def dfs(i):
11            if i<0:
12                return 1
13            res=0
14            if s[i]!="0":
15                res+= dfs(i-1)
16            
17            if i-1>=0 and 10<=int(s[i-1:i+1])<=26:
18                res+=dfs(i-2)
19            
20            return res
21        return dfs(n-1)
22
23
24      
25