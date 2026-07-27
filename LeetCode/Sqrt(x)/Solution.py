1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x==0 or x==1:
4            return x
5        
6        l,r=0,x//2
7        while l<=r:
8            mid= (r+l)//2
9            if mid*mid==x:
10                return mid
11            elif mid*mid>x:
12                r=mid-1
13            else:
14                l=mid+1
15        return r