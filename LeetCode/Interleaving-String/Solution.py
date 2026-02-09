1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        m,n=len(s1),len(s2)
4        # Pruning
5        if m+n!=len(s3):
6            return False
7        @lru_cache(None)
8        def dfs(i,j):
9            if i==0 and j==0:
10                return True
11            k=i+j-1
12            if i>0 and s1[i-1]==s3[k] and dfs(i-1,j):
13                return True
14            if j>0 and s2[j-1]==s3[k] and dfs(i,j-1):
15                return True
16            return False
17        return dfs(m,n)
18