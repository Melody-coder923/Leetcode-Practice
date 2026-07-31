1class Solution:
2    def gcdOfOddEvenSums(self, n: int) -> int:
3        odd_sum = 0
4        even_sum = 0
5
6        for i in range(1, n + 1):
7            odd_sum += 2 * i - 1
8            even_sum += 2 * i
9
10        return math.gcd(odd_sum, even_sum)
11    
12
13