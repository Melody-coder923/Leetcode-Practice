class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def is_palindrom(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return (l+1,r-1)
      
        longest=0
        
        for i in range(n):
            l,r=is_palindrom(i,i)
            if r-l+1>longest:
                longest=r-l+1
                res=s[l:r+1]
            
            l,r=is_palindrom(i,i+1)
            if r-l+1>longest:
                longest=r-l+1
                res=s[l:r+1]

        
        return res

