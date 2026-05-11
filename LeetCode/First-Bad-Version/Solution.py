1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        l,r=1,n        #找好的最后一个      
7        while l<=r:
8            mid=(l+r)//2
9            if isBadVersion(mid)==True:
10                r=mid-1  #mid是坏的,好的在左边
11            elif isBadVersion(mid)==False:
12                l=mid+1   #mid是好的,好的在右边
13            
14        return l 