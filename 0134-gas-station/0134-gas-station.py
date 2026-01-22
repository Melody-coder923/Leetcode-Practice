class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total, curr = 0, 0
        start=0
        for i in range(n):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                # 当前 start 到 i 无法作为起点，跳过
                start = i + 1
                curr = 0
        return start if total >= 0 else -1