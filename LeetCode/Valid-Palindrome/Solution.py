1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        n=len(s)
4        if n<=1:
5            return True
6        s=s.lower()
7        l,r=0,len(s)-1
8        while l<r:
9            while l < r and not s[l].isalnum():
10                l += 1
11            while l < r and not s[r].isalnum():
12                r -= 1
13        
14            if s[l]!=s[r]:
15                return False
16            l+=1
17            r-=1
18        return True
19