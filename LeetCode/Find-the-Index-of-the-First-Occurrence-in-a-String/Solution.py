1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        n=len(haystack)
4        m=len(needle)
5        if m==0:
6            return 0
7        next_arr = self.buildnext_arr(needle)
8        j=0
9        for i in range(n):
10            while j > 0 and haystack[i] != needle[j]:
11                j = next_arr[j - 1]
12            if haystack[i] == needle[j]:
13                j += 1
14            if j==m:
15                return i-m+1
16        return -1
17    def buildnext_arr(self, pattern:str) ->List[int]:
18        m=len(pattern)
19        next_arr=[0] * m
20        j=0
21        for i in range(1,m):
22            while j > 0 and pattern[i] != pattern[j]:
23                j = next_arr[j - 1]
24            if pattern[i] == pattern[j]:
25                j += 1
26            next_arr[i] = j
27        return next_arr
28    
29
30                    
31
32