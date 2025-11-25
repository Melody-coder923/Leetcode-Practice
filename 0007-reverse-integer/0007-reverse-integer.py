class Solution:
    def reverse(self, x: int) -> int:
        #step1: 符号
        sign = -1 if x < 0 else 1
        #step2:% 取前面数 ,// 带到下一轮 
        res=0
        x=abs(x)
        while x>0: #123, 12, 1
            mod=x%10 # 3,2, 1
            x=x//10 # 12,1, 0
            res= res*10+mod # 3 , 32, 321
        res=res*sign
        if res<-2**31 or res>2**31-1:
            return 0
        return res