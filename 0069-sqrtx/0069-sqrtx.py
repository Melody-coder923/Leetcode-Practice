class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        while l<=r:
            mid=(l+r)//2
            if mid*mid==x:
                return mid 
            elif mid*mid>x:
                r=mid-1
            else:
                l=mid+1
        return r # l在r的右边, r是最后一个小于target的数