1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        @lru_cache(None)
4        def dfs(i,j):     
5            if i==0 or j==0:
6                return 1
7            
8            return dfs(i-1,j)+dfs(i,j-1)
9
10        return dfs(m-1,n-1)
11    