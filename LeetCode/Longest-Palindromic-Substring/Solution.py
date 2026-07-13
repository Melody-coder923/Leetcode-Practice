1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n=len(s)
4        def expand(l,r):
5            while l>=0 and r<n and s[l]==s[r]:
6                l-=1
7                r+=1
8            return s[l+1:r]
9        res=""
10        for i in range(n):
11            single=expand(i,i)
12            double=expand(i,i+1)
13            if len(single)>len(res):
14                res=single
15            if len(double)>len(res):
16                res=double
17        
18        return res