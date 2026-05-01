1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n=len(s)
4        @lru_cache(None)
5        def dfs(i): # 从下标 i 开始，s[i:] 有多少种解码方式
6            # base case
7            if i<0:
8                return 1
9
10            res = 0
11            # 单个数字 个位 1-9
12            if s[i] != '0':
13                res += dfs(i - 1)
14            #两个数字 十位 10-26
15            if i-1>=0 and 10 <= int(s[i-1:i+1]) <= 26:
16                res += dfs(i-2)
17
18            return res
19        return dfs(n-1)