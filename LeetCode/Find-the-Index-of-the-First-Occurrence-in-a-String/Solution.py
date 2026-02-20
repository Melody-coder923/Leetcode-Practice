1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if not needle:
4            return -1
5        if not haystack or len(needle) > len(haystack):
6            return -1
7        def build_next(pattern):
8            n = len(pattern)
9            next_arr = [0] * n
10            j = 0
11            for i in range(1, n):
12            # 不匹配时回退
13                while j > 0 and pattern[i] != pattern[j]:
14                    j = next_arr[j-1]
15            # 匹配时前进
16                if pattern[i] == pattern[j]:
17                    j += 1
18            # 设置 next 值
19                next_arr[i] = j
20            return next_arr
21        next_arr = build_next(needle)
22        n, m = len(haystack), len(needle)
23        j = 0  # 模式串指针
24        for i in range(n):  # i 是主串指针
25        # 处理不匹配：j 回退，i 不动
26            while j > 0 and haystack[i] != needle[j]:
27                j = next_arr[j-1]
28        # 处理匹配：双指针都前进
29            if haystack[i] == needle[j]:
30                j += 1
31        
32        # 检查完全匹配
33            if j == m:
34                return i - m + 1  # 返回匹配的起始位置
35    
36        return -1  # 未找到匹配