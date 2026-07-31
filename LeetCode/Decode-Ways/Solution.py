1class Solution:
2    def numDecodings(self, s: str) -> int:
3        #edge case
4        n=len(s)
5        if n==1 and s[0]!="0":
6            return 1
7        if s[0]=="0":
8            return 0
9        
10        @lru_cache(None)
11        def dfs(i):
12            #base case
13            if i<0:
14                return 1
15            res=0
16            #single
17            if s[i]!="0":
18                res+=dfs(i-1)
19            
20            #double
21            if i-1>=0 and 10<=int(s[i-1:i+1])<=26:
22                res+=dfs(i-2)
23            
24            return res
25        
26        return dfs(n-1)