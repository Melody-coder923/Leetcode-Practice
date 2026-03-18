1class Solution:
2    def climbStairs(self, n: int) -> int:
3        memo = {}
4        def dfs(rest):
5            if rest < 0:
6                return 0
7            if rest == 0:
8                return 1
9            if rest in memo:
10                return memo[rest]
11            memo[rest] = dfs(rest - 1) + dfs(rest - 2)
12            return memo[rest]
13        return dfs(n)