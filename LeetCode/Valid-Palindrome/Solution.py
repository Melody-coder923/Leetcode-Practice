1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = s.lower()
4        l,r=0,len(s)-1
5        while l<r:
6            if not s[l].isalnum():
7                l+=1
8                continue
9            if not s[r].isalnum():
10                r-=1
11                continue
12            if s[l]!=s[r]:
13                return False
14            l += 1
15            r -= 1
16        return True
17            