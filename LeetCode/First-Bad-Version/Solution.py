1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        l,r=0,n+1
7        while l<r:
8            mid=l+(r-l)//2
9            if isBadVersion(mid):
10                r=mid
11            else:
12                l=mid+1
13        return l
14
15