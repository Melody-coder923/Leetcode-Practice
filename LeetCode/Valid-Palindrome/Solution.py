1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        if len(s)<=1:
4            return True
5        s=s.lower()
6        left,right=0,len(s)-1
7        while left<right:
8            if not s[left].isalnum():
9                left+=1
10            elif not s[right].isalnum():
11                right-=1
12            elif s[left]!=s[right]:
13                return False
14            else:
15                left+=1
16                right-=1
17        return True
18            