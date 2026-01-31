class Solution:
    def trailingZeroes(self, n: int) -> int:
        res=0
        #一个5的阶乘贡献1个0
        divisor=5
        while divisor<=n: 
            res+=n//divisor
            divisor*=5
        return res