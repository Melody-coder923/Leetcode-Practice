1class Solution:
2    def reverse(self, x: int) -> int:
3        sign=-1 if x<0 else 1
4        num=abs(x)
5        res=0
6        while num>0:
7            mod=num%10 
8            num=num//10
9            res=res*10+mod 
10        
11        res=res*sign
12        if res<-2**31 or res>2**31-1:
13            return 0
14        else:
15            return res
16