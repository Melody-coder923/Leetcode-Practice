1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if not needle:
4            return -1
5        if not haystack or len(needle) > len(haystack):
6            return -1
7        for i in range(len(haystack) - len(needle) + 1):
8            if haystack[i:i+len(needle)] == needle:
9                return i
10        return -1