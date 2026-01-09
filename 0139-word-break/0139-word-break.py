class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       # 前缀 DP / 字符串切分 DP（Prefix DP）
       #关键点只有一个：切位置, dp[i]：s 的前 i 个字符，能不能被成功拆分
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        
        # 空字符串 一定可以被拆分
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]