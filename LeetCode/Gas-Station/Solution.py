1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        n=len(gas)
4        cur=total=0
5        start=0
6        for i in range(n):
7            total += gas[i] - cost[i]
8            cur += gas[i] - cost[i]
9            if cur<0:
10                start=i+1
11                cur=0
12        return start if total>=0 else -1