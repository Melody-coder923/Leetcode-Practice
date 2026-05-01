1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s)
4        count=0
5        def expand(l,r):
6            nonlocal count
7            while l>=0 and r<n and s[l]==s[r]:
8                l -= 1
9                r += 1
10                count+=1
11        
12        for i in range(n):
13            expand(i,i)
14            expand(i,i+1)
15        
16        return count