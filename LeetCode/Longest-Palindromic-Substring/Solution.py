1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        def expand(l,r):
4            while l>=0 and r<len(s) and s[l]==s[r]:
5                l-=1
6                r+=1
7            return l+1,r-1
8        
9        maxlen=0
10        res=""
11        for i in range(len(s)):
12            l,r=expand(i,i)
13            length = r - l + 1
14            if length>maxlen:
15                maxlen=length
16                res=s[l:r+1]
17
18            l,r=expand(i,i+1)
19            length = r - l + 1
20            if length>maxlen:
21                maxlen=length
22                res=s[l:r+1]
23        
24        return res
25            
26