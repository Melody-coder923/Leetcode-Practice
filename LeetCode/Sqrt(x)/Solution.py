1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x<=1:
4            return x
5
6        l,r=1,x//2
7        while l<=r:
8            mid=(l+r)//2
9            if mid*mid==x:
10                return mid
11
12            elif mid*mid<x:
13                l=mid+1
14            else:
15                r=mid-1
16        return r