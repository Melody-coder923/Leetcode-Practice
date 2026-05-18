1class Solution:
2    def maxRunTime(self, n: int, batteries: List[int]) -> int:
3        l,r=0,sum(batteries)//n #时间范围： 最小到最大的时间
4        while l<=r:
5            mid=(l+r)//2 
6            power = sum(min(b, mid) for b in batteries) #如果目标是让所有 n 台电脑同时运行 mid 分钟，所有电池最多能“贡献”的总电量，need = n * mid
7            if power>=mid*n:
8                l=mid+1
9            else:
10                r=mid-1
11        return r
12        #停下来的时候l>r        
13