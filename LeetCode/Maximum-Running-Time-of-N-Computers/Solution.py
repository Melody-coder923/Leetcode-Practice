1class Solution:
2    def maxRunTime(self, n: int, batteries: List[int]) -> int:
3        l,r=0,sum(batteries)//n
4        while l<r:
5            mid = (l + r + 1) // 2
6            power = sum(min(b, mid) for b in batteries)
7            if power >= mid * n:
8                l = mid
9            else:
10                r = mid - 1
11        return l