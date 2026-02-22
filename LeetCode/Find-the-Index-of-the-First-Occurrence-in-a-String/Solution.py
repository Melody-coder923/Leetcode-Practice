1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        def buildnext(s):
4            n=len(s)
5            nxt=[0]*n
6            j=0
7            for i in range(1,n):
8                while j>0 and s[i]!=s[j]:
9                    j=nxt[j-1]  
10                if s[i]==s[j]:   
11                    j+=1
12                nxt[i]=j
13            return nxt
14        n,m=len(needle),len(haystack)
15        if n==0:
16            return 0
17        if n>m:
18            return -1
19        nxt=buildnext(needle)
20        j=0
21        for i in range(m):
22            while j>0 and haystack[i] != needle[j]:
23                j=nxt[j-1]
24            if haystack[i] == needle[j]:
25                j += 1
26            if j==n:
27                return i-j+1
28        return -1
29                
30            
31
32