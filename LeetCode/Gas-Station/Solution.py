1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        n=len(gas)
4        cur=total=0
5        start=0
6
7        for i in range(n):
8            cur= cur+gas[i]-cost[i]
9            total=total+gas[i]-cost[i]
10
11            if cur<0:
12                cur=0
13                start=i+1
14        return start if total>=0 else -1