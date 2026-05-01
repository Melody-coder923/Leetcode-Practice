1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s)
4        count = 0
5
6        # 遍历字符串中的每一个字符，将其作为中心
7        for i in range(n):
8            # --- 情况 1: 回文串长度为奇数 ---
9            # 中心是单个字符 s[i]
10            l, r = i, i
11            while l >= 0 and r < n and s[l] == s[r]:
12                count += 1  # 发现一个回文串
13                l -= 1      # 向左扩展
14                r += 1      # 向右扩展
15
16            # --- 情况 2: 回文串长度为偶数 ---
17            # 中心是两个字符 s[i] 和 s[i+1]
18            l, r = i, i + 1
19            while l >= 0 and r < n and s[l] == s[r]:
20                count += 1  # 发现一个回文串
21                l -= 1      # 向左扩展
22                r += 1      # 向右扩展
23        
24        return count