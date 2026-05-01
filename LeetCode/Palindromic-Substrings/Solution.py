1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n=len(s)
4        if n==1:
5            return 1
6        count=0
7        @lru_cache(None)
8        def dfs(l,r):
9            if l>=r:
10                return True
11            return dfs(l+1, r-1) and s[l] == s[r]
12        
13        for i in range(n):
14            for j in range(i,n):
15                if dfs(i,j):
16                    count+=1
17        
18        return count
19                
20