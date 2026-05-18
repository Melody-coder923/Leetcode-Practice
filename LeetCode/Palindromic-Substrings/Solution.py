1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n=len(s)
4        count=0
5        def expand(l,r):
6            nonlocal count
7            while l>=0 and r<n and s[l]==s[r]:
8                count+=1
9                l-=1
10                r+=1
11        for i in range(n):
12            expand(i,i)
13            expand(i,i+1)
14        return count