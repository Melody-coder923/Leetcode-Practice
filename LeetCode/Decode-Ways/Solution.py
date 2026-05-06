1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4
5        @lru_cache(None)
6        def dfs(i):  # 表示 s[:i] 的解码方式
7            if i == 0:
8                return 1
9
10            res = 0
11
12            # 单个字符（看 s[i-1]）
13            if s[i-1] != "0":
14                res += dfs(i-1)
15
16            # 两个字符（看 s[i-2:i]）
17            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
18                res += dfs(i-2)
19
20            return res
21
22        return dfs(n)