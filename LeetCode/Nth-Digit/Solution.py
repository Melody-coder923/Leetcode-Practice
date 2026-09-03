1class Solution:
2    def findNthDigit(self, n: int) -> int:
3        d = 1
4        count = 9
5        while n > d * count:
6            n -= d * count
7            d += 1
8            count *= 10
9        
10        start = 10 ** (d - 1)
11        num = start + (n - 1) // d
12        idx = (n - 1) % d
13        return int(str(num)[idx])