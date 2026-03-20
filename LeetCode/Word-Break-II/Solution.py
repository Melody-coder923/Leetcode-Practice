1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
3        # dp[i] 以i为结尾看前缀是否能凑出来, 存的列表
4        n=len(s)
5        dp = [[] for _ in range(n + 1)]
6        # 初始化dp
7        dp[0]= [""]
8
9        wordDict=set(wordDict)
10       # 填充dp
11        for i in range(n+1):
12            for j in range(i):
13                if s[j:i] in wordDict:
14                    suffix=s[j:i]
15                    tmp=dp[j]
16                    for word in tmp:
17                        dp[i].append((word+" "+suffix).strip())
18        return dp[n]
19                    
20
21
22
23