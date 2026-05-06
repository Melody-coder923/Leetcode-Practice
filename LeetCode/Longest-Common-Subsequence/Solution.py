1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m, n = len(text1), len(text2)
4        dp = [[0] * (n + 1) for _ in range(m + 1)]
5        for i in range(1, m + 1):
6            for j in range(1, n + 1):
7                if text1[i - 1] == text2[j - 1]:
8                    dp[i][j] = dp[i - 1][j - 1] + 1
9                else:
10                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
11        return dp[m][n]