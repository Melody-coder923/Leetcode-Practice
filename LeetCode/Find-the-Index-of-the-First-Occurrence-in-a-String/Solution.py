1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if not needle:
4            return 0
5        def build_next(pattern: str):
6            n = len(pattern)
7            next = [-1] * n
8            j = -1
9            for i in range(1, n):
10                while j != -1 and pattern[i - 1] != pattern[j]:
11                    j = next[j]
12                j += 1
13                next[i] = j
14            return next
15        next = build_next(needle)
16        j = 0
17        for i in range(len(haystack)):
18            while j > 0 and haystack[i] != needle[j]:
19                j = next[j]
20            if haystack[i] == needle[j]:
21                j += 1
22            if j == len(needle):
23                return i - j + 1
24        return -1
25