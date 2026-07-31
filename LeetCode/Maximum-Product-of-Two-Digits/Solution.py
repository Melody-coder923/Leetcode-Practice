1class Solution:
2    def maxProduct(self, n: int) -> int:
3        digits = []
4        while n > 0:
5            digit = n % 10
6            digits.append(digit)
7            n //= 10
8        digits.sort()
9
10        return digits[-1] * digits[-2]