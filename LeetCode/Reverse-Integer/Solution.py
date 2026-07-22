1class Solution:
2    def reverse(self, x: int) -> int:
3        sign=-1 if x<0 else 1
4        num=abs(x)
5        mod=0
6        res=0
7        while num>0:
8            mod=num%10 
9            num=num//10
10            res=res*10+mod 
11        
12        res=res*sign
13        if res<-2**31 or res>2**31-1:
14            return 0
15        else:
16            return res
17