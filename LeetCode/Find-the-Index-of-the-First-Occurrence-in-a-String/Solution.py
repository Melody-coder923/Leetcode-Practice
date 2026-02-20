1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if needle == "":
4            return 0
5        n=len(needle)
6        f=needle[0]
7        for i, char in enumerate(haystack):
8            if char==f:
9                if haystack[i:i+n]==needle:
10                    return i
11        return -1