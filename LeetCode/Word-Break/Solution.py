1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3       # 前缀 DP / 字符串切分 DP（Prefix DP）
4       #关键点只有一个：切位置, dp[i]：s 的前 i 个字符，能不能被成功拆分
5        wordSet = set(wordDict)
6        n = len(s)
7        dp = [False] * (n + 1)
8        
9        # 空字符串 一定可以被拆分
10        dp[0] = True
11
12        for i in range(1, n + 1):
13            for j in range(i):
14                if dp[j] and s[j:i] in wordSet:
15                    dp[i] = True
16                    break
17        return dp[n]