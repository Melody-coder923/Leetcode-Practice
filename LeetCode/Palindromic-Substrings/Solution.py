1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s)
4        dp = [[False] * n for _ in range(n)]
5        count = 0
6        for i in range(n - 1, -1, -1):
7            for j in range(i, n):
8                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):
9                    dp[i][j] = True
10                    count += 1
11
12        return count