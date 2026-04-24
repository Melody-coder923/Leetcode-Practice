1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n<=2:
4            return n
5            
6        @lru_cache(None)
7        def dfs(n):
8            #base case
9            if n<=2:
10                return n
11
12            # break down problems 
13            return dfs(n-1)+dfs(n-2)
14
15        return dfs(n)