1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n=len(s)
4        count=0
5
6        def expand(l,r):
7            nonlocal count
8            while l >= 0 and r < n and s[l] == s[r]:
9                count+=1
10                l-=1
11                r+=1
12    
13
14        for i in range(n):
15            expand(i,i)
16            expand(i,i+1)
17        return count
18            