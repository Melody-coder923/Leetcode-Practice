1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        count = Counter(tasks)
4        maxFreq = max(count.values())
5        maxCount = list(count.values()).count(maxFreq)
6
7        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)