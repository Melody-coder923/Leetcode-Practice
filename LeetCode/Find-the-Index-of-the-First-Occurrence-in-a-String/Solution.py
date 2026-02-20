1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if not needle:
4            return 0
5        for i in range(len(haystack)-len(needle)+1):
6            for j in range(len(needle)):
7                if haystack[i+j]!=needle[j]:
8                    break
9            else:
10                return i
11        return -1