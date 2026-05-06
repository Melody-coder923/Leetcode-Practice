1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4        prev2=1
5        prev1=0 if s[0]=="0" else 1
6
7        for i in range(2,n+1):
8            curr=0
9            if s[i-1]!="0":
10                curr+=prev1
11
12            twodigit=int(s[i-2:i])
13            if 10<= twodigit<=26:
14                curr+=prev2
15            
16            prev2,prev1=prev1,curr
17
18        return prev1