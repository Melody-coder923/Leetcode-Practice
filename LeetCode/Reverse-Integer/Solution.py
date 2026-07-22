1class Solution:
2    def reverse(self, x: int) -> int:
3        sign=-1 if x<0 else 1
4
5        num=abs(x)
6        new_num=0
7        while num>0:
8            keep=num%10 #3,2 , 1
9            num=num//10  # 12,1 0
10            new_num=new_num*10+keep # 3, 2, 1
11        
12        res=new_num*sign 
13        if res<-2**31 or res>2**31-1:
14            return 0
15        return res