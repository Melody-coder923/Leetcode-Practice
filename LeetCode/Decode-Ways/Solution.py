1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4        if s[0]=="0":
5            return 0
6        dp = [0] * (n + 1)  #dp[i] = s[0:i] 这一段前 i 个字符，有多少种解码方式，s[0:i] 不包含下标 i。
7        dp[0] = 1 # 为了让dp[2] += dp[0]成立，所以必须为1
8        dp[1] = 0 if s[0] == '0' else 1
9
10        for i in range(2, n + 1):
11            if s[i-1] != '0':
12                dp[i] += dp[i-1]
13            two_digit = int(s[i-2:i])
14            if 10 <= two_digit <= 26:
15                dp[i] += dp[i-2]
16        return dp[n]
17