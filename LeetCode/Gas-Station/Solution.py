1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        n = len(gas)
4        total, curr = 0, 0
5        start=0
6        for i in range(n):
7            total += gas[i] - cost[i]
8            curr += gas[i] - cost[i]
9            if curr < 0:
10                # 当前 start 到 i 无法作为起点，跳过
11                start = i + 1
12                curr = 0
13        return start if total >= 0 else -1