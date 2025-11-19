class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:   # n 是奇数
                result *= x
            x *= x            # x 翻倍
            n //= 2           # n 减半
        return result
"""
核心思想：利用 指数分解，把指数每次减半
时间复杂度：O(log n)，指数每次都减半。
"""