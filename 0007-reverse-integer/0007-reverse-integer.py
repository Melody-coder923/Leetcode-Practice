class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1

        num=abs(x)
        new_num=0
        while num>0:
            keep=num%10 #3,2 , 1
            num=num//10  # 12,1 0
            new_num=new_num*10+keep # 3, 2, 1
        
        res=new_num*sign 
        if res<-2**31 or res>2**31-1:
            return 0
        return res