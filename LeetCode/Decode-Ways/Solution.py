1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4        if n == 0: return 0
5        dp = [0] * (n + 1)
6        dp[0] = 1
7        dp[1] = 0 if s[0] == '0' else 1
8
9        for i in range(2, n + 1):
10            if s[i-1] != '0':
11                dp[i] += dp[i-1]
12            two_digit = int(s[i-2:i])
13            if 10 <= two_digit <= 26:
14                dp[i] += dp[i-2]
15        return dp[n]
16