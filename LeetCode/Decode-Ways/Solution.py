1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4
5        # dp[0]
6        prev2 = 1
7
8        # dp[1]
9        prev1 = 0 if s[0] == '0' else 1
10
11        for i in range(2, n + 1):
12            curr = 0
13
14            # 最后 1 位单独解码
15            if s[i - 1] != '0':
16                curr += prev1
17
18            # 最后 2 位一起解码
19            two_digit = int(s[i - 2:i])
20            if 10 <= two_digit <= 26:
21                curr += prev2
22
23            # 往后滚动
24            prev2, prev1 = prev1, curr
25
26        return prev1