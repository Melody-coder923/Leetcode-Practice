1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n=len(s)
4        if n==1:
5            return 1
6        count=0
7        for i in range(n):
8            l,r=i,i
9            while l>=0 and r<n and s[l]==s[r]:
10                count+=1
11                l-=1
12                r+=1
13            
14            l,r=i,i+1
15            while l>=0 and r<n and s[l]==s[r]:
16                count+=1
17                l-=1
18                r+=1
19        
20        return count
21