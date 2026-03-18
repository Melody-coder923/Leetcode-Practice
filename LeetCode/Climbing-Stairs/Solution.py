1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 1:
4            return 1
5        prev, curr = 1, 1
6        for i in range(2, n + 1):
7            prev, curr = curr, prev + curr
8        return curr
9       